var get_tweet_html = function(author_name, author_pic_url, text, date) {
    var html = '<div class="row-fluid hide"><div class="tweet span6 offset3">' +
        '<span class="author"><img src="'+author_pic_url+'" class="img-rounded">' +
        '&nbsp;'+author_name+'</span>&nbsp;<span class="date">' + prettyDate(date) + '</span>' +
        '<p>'+text+'</p>'+
    '</div></div>';
    return html;
}

function TweetUpdater() {
}

TweetUpdater.latest_id = 0;
TweetUpdater.undisplayed_tweets = new Array();

TweetUpdater.prototype.get_more_tweets = function () {
    var get_tweets_url = "/showtweets/?after_id="+TweetUpdater.latest_id;
    $.get(get_tweets_url, function (tweets) {
        if (tweets.length > 0) {
            TweetUpdater.latest_id = tweets[0].id;
            for (var i = 0; i < tweets.length; i++) {
                TweetUpdater.undisplayed_tweets.push(tweets[i]);
            }
        }
    }, "json");
};

TweetUpdater.prototype.show_more_tweets = function () {
    while (TweetUpdater.undisplayed_tweets.length > 0) {
        $('.notweet').remove();
        tweet = TweetUpdater.undisplayed_tweets.pop();

        $('#tweetcontainer').prepend(get_tweet_html(
            tweet.author,
            tweet.author_pic_url,
            tweet.text,
            tweet.date));

        $("#tweetcontainer").find(">:first-child").fadeIn("slow");
    }
};

GET_TWEET_INTERVAL = 5000;
SHOW_TWEET_INTERVAL = 1000;
var tweetupdater = new TweetUpdater();
$(function(){
    setInterval(tweetupdater.get_more_tweets, GET_TWEET_INTERVAL);
    setInterval(tweetupdater.show_more_tweets, SHOW_TWEET_INTERVAL);
});