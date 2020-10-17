from time import sleep
import os
import random

import requests


KEY = os.environ['THING_SPEAK_WRITER_API_KEY']
BASE_URL = f'https://api.thingspeak.com/update?api_key={KEY}'

while True:
    VALUE = random.randint(0, 100)
    requests.get(f'{BASE_URL}&field1={VALUE}')
    sleep(10)
