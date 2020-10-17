from time import sleep
from datetime import date
import random
import os

import telepot
import psutil


def get_cpu_percentage():
    return f'CPU usage is at {psutil.cpu_percent()}%'


def get_random_phrase():
    messages = [
        'Some',
        'random',
        'responses'
    ]
    return random.choice(messages)


def get_current_date():
    today = date.today()
    return f'Today is {today.strftime("%d/%m/%Y")}'


TOKEN = os.environ['TELEGRAM_TOKEN']
BOT = telepot.Bot(TOKEN)
OPTIONS = {
    'cpu_percentage': get_cpu_percentage,
    'random_phrase': get_random_phrase,
    'current_date': get_current_date
}


def get_response(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command in OPTIONS.keys():
        BOT.sendMessage(chat_id, OPTIONS[command]())


BOT.message_loop(get_response)

while True:
    sleep(1)
