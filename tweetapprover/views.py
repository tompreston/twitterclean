from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from tweetapprover.models import ApprovableTweet
from datetime import datetime
from django.utils import simplejson
import time
import twitter


SEARCH_TERM = "#raspberrypi"

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

OAUTH_TOKEN = ""
OAUTH_SECRET = ""


def index(request):
    try:
        tweet = ApprovableTweet.objects.filter(status=ApprovableTweet.PENDING)
        tweet = tweet.order_by('tweet_date')[0]
    except IndexError:
        return render_to_response('twitterapprover/no_pending_tweets.html', {
            'time': datetime.now(),
        })
    else:
        return render_to_response('twitterapprover/index.html', {
            'tweet_id': tweet.tweet_id,
            'tweet_text': tweet.tweet_text,
        })


def approve(request, tweet_id):
    try:
        tweet = ApprovableTweet.objects.get(tweet_id=tweet_id)
        tweet.status = ApprovableTweet.APPROVED
        tweet.save()
    except Exception as e:
        message = { 'approved': False, 'message': e}
        return HttpResponse(
            simplejson.dumps(message), mimetype="application/json")
    else:
        message = { 'approved': True, 'message': 'Tweet was approved.'}
        return redirect(index)


def deny(request, tweet_id):
    try:
        tweet = ApprovableTweet.objects.get(tweet_id=tweet_id)
        tweet.status = ApprovableTweet.DENIED
        tweet.save()
    except Exception as e:
        message = { 'denied': False, 'message': e}
        return HttpResponse(
            simplejson.dumps(message), mimetype="application/json")
    else:
        message = { 'denied': True, 'message': 'Tweet was denied.'}
        # return HttpResponse(
        #     simplejson.dumps(message), mimetype="application/json")
        return redirect(index)


def getmoretweets(request):
    t = twitter.Twitter(auth=twitter.OAuth(
            OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
    try:
        latest_db_tweet = ApprovableTweet.objects.latest('tweet_date')
    except ApprovableTweet.DoesNotExist:
        latest_tweets = t.search.tweets(q=SEARCH_TERM)['statuses']
    else:
        last_id = latest_db_tweet.tweet_id
        latest_tweets = t.search.tweets(
            q=SEARCH_TERM, since_id=last_id)['statuses']

    for tweet in latest_tweets:
        approvabletweet = ApprovableTweet()
        approvabletweet.status
        approvabletweet.tweet_id = tweet['id']
        approvabletweet.tweet_text = tweet['text']
        created_time = datetime(*(time.strptime(
            tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')[0:6]))
        approvabletweet.tweet_date = created_time
        approvabletweet.tweet_author = tweet['user']['name']
        approvabletweet.tweet_author_pic_url = tweet['user']['profile_image_url']
        approvabletweet.save()

    message = {
        'message': 'Added {} more tweets.'.format(len(latest_tweets)),
        'tweets_added': len(latest_tweets),
    }
    # return HttpResponse(simplejson.dumps(message), mimetype="application/json")
    return redirect(index)
