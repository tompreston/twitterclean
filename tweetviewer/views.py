from django.http import HttpResponse
from django.shortcuts import render_to_response
from tweetapprover.models import ApprovableTweet
from tweetapprover.views import get_search_term
from django.utils import simplejson
from datetime import datetime


def showtweets(request):
    """Displays the approved tweets with JSON."""
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
    after_id = request.GET.get('after_id')
    return HttpResponse(
        simplejson.dumps(get_tweets(after_id), default=dthandler),
        mimetype="application/json")


def index(request):
    """Displays approved tweets in a nice format."""
    after_id = request.GET.get('after_id')
    return render_to_response('twitterviewer/index.html', {
        'searchterm': get_search_term(),
        # 'tweets': get_tweets(after_id),
    })


def get_tweets(after_id=None):
    tweets = ApprovableTweet.objects.filter(status=ApprovableTweet.APPROVED)
    if after_id:
        tweets = tweets.filter(tweet_id__gt=after_id)
    return [{
        'id': str(tweet.tweet_id),
        'text': tweet.tweet_text,
        'author': tweet.tweet_author,
        'date': tweet.tweet_date,
        'author_pic_url': tweet.tweet_author_pic_url,
        } for tweet in tweets]
