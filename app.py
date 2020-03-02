#!/usr/bin/env python3
import os

import telepot
import telepot.loop


with open('token.txt') as tok:
    TOKEN = tok.read().strip()

BOT = telepot.Bot(TOKEN)

def handle(msg):
    sender = msg['from']['id']
    chat = msg['chat']['id']
    if msg['chat']['type'] == 'private':
        BOT.sendMessage(chat, "Я не поняла")
        BOT.sendMessage(chat, f"А что значит \"{msg['text']}\"?")

BOT.deleteWebhook()
telepot.loop.MessageLoop(BOT, handle).run_forever()
