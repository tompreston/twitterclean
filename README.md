twitterclean
============

A simple tweet cleaner for displaying tweets at public events.

Uses Django 1.2.3 (shouldn't be too difficult to port to another version, just
fiddling with some of the settings). To install Django 1.2.3:

    pip install Django=1.2.3

Also requires [twitter](https://pypi.python.org/pypi/twitter):

    pip install twitter

Use
===

- Edit `setting.py` and `urls.py` to point to /wherever/you/placed/twitterclean/ (several changes).
- Add your Oauth stuff in twitterviewer/views.py
- Make sure you generate the database: `python manage.py syncdb`

Run with (Get your IP first: `hostname -I`):

    python manage.py runserver 0.0.0.0:8000


To view approved tweets: `http://yourip:8000`

To approve/deny tweets: `http://yourip:8000/approvetweets/`

To view approved tweets as JSON: `http://yourip:8000/showtweets/`

To view approved tweets as JSON after a certain tweet id: `http://yourip:8000/showtweets/?after_id=12345678`
