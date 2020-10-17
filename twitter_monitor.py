from time import sleep
import os
import random
import requests


BASE_URL = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'
TIME_BETWEEN_WARNINGS_MINUTES = int(os.environ['TIME_BETWEEN_WARNINGS_MINUTES'])
KEY = os.environ['THING_TWEET_API_KEY']

def notification():
    status = 'Suspicious activity on premises, check cameras!'
    body = {'api_key': KEY, 'status': status}
    requests.post(BASE_URL, data=body)


def current_motion_detection():
    return random.randint(0, 1)


while True:
    motion = current_motion_detection()
    if motion == 1:
        notification()
        sleep(TIME_BETWEEN_WARNINGS_MINUTES * 60)
    sleep(1)
