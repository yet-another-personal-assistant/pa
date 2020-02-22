#!/usr/bin/env python3
import os

from queue import Queue

from flask import Flask, request
import telepot


app = Flask(__name__)
TOKEN = os.environ['BOT_TOKEN']
SECRET = f'/bot{TOKEN}'
URL = os.environ['HEROKU_URL']

UPDATE_QUEUE = Queue()
BOT = telepot.Bot(TOKEN)

def handle(msg):
    sender = msg['from']['id']
    chat = msg['chat']['id']
    if msg['chat']['type'] == 'private':
        BOT.sendMessage(chat, "Я не поняла")
        BOT.sendMessage(chat, f"А что значит \"{msg['text']}\"?")

BOT.message_loop({'chat': handle}, source=UPDATE_QUEUE)


@app.route(SECRET, methods=['GET', 'POST'])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return 'OK'


if os.getenv('BOT_SET_WEBHOOK') is not None:
    import time
    time.sleep(5)
    BOT.setWebhook(URL + SECRET)
