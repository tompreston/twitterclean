twitterclean
============

A simple tweet cleaner for displaying tweets at public events.

Uses Django 1.2.3 (shouldn't be too difficult to port to another version, just
fiddling with some of the settings.py). To install Django 1.2.3:

    pip install Django=1.2.3

You will have to be root (or use sudo) and make sure you don't already have
Django installed (or use virtualenv).

Use
===

Edit `setting.py` to point to /wherever/you/placed/twitterclean/ in several places and make sure you generate the database with:

    python manage.py syncdb

Run with (get your IP first: `hostname -I`):

    python manage.py runserver 0.0.0.0:8000


To view approved tweets: `http://yourip:8000`

To approve/deny tweets: `http://yourip:8000/approvetweets/`

To view approved tweets as JSON: `http://yourip:8000/showtweets/`

To view approved tweets as JSON after a certain tweet id: `http://yourip:8000/showtweets/?after_id=12345678`


Examples
========

twitterspeak
------------
Uses a RaspberryPi and PiFace to wobble a chicken and say the approved tweets.