from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'tweetviewer.views.index'),
    (r'^showtweets/', 'tweetviewer.views.showtweets'),
    (r'^approvetweets/$', 'tweetapprover.views.index'),
    (r'^approvetweets/approve/(?P<tweet_id>\d+)', 'tweetapprover.views.approve'),
    (r'^approvetweets/deny/(?P<tweet_id>\d+)', 'tweetapprover.views.deny'),
    (r'^getmoretweets/', 'tweetapprover.views.getmoretweets'),

    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': "/home/tom/Work/pifacehome/twitterclean/static/css/" }),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': "/home/tom/Work/pifacehome/twitterclean/static/js/" }),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
