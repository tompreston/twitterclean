from django.db import models


class ApprovableTweet(models.Model):
    PENDING = 'p'
    APPROVED = 'a'
    DENIED = 'd'
    STATUS_TEXT = {
        PENDING: 'Pending',
        APPROVED: 'Approved',
        DENIED: 'Denied',
    }
    TWEET_STATUSES = (
        (PENDING, STATUS_TEXT[PENDING]),
        (APPROVED, STATUS_TEXT[APPROVED]),
        (DENIED, STATUS_TEXT[DENIED]),
    )
    status = models.CharField(
        max_length=1,
        choices=TWEET_STATUSES,
        default=PENDING)
    tweet_id = models.IntegerField(primary_key=True)
    tweet_text = models.CharField(max_length=170)
    tweet_author = models.CharField(max_length=50)
    tweet_date = models.DateTimeField()
    tweet_author_pic_url = models.CharField(max_length=200)

    def __unicode__(self):
        return "Tweet ({status})".format(
            status=ApprovableTweet.STATUS_TEXT[self.status])
