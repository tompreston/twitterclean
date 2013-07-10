#!/usr/bin/env python3
import json
import subprocess
import urllib.request
from time import sleep
import pifacedigitalio


CLEAN_TWEET_URL = "http://192.168.1.250:8000/showtweets/"
CHICKEN_RELAY = 0
DELAY = 5


class RobotChicken(pifacedigitalio.Relay):
    def __init__(self):
        super().__init__(CHICKEN_RELAY)

    def say(self, message):
        subprocess.call(["espeak", message])


def get_latest_tweet(after_id):
    clean_tweets = urllib.request.urlopen("{}?after_id={}".format(
        CLEAN_TWEET_URL, after_id)).read().decode('utf-8')
    try:
        latest_tweet = json.loads(clean_tweets)[0]
    except IndexError:
        latest_tweet = None
    finally:
        return latest_tweet


def say_latest_tweet(robotchicken):
    global last_tweet_id
    latest_tweet = get_latest_tweet(last_tweet_id)
    if latest_tweet and latest_tweet['id'] != last_tweet_id:
        last_tweet_id = latest_tweet['id']
        robotchicken.turn_on()
        print("Saying:", latest_tweet['text'])
        robotchicken.say(latest_tweet['text'])
        robotchicken.turn_off()


def main():
    global last_tweet_id
    last_tweet_id = 0

    pifacedigitalio.init()
    robotchicken = RobotChicken()

    try:
        while True:
            say_latest_tweet(robotchicken)
            sleep(DELAY)
    except KeyboardInterrupt:
        pifacedigitalio.deinit()


if __name__ == '__main__':
    main()
