import json
import logging
from functools import partial

import stomp
import telepot
import telepot.loop


_LOGGER = logging.getLogger(__name__)


def _for_each(maybe_list, func):
    if isinstance(maybe_list, list):
        for item in maybe_list:
            func(item)
    else:
        func(maybe_list)


class Tg(stomp.ConnectionListener):

    def __init__(self, token, conn):
        self.bot = telepot.Bot(token)
        self.connection = conn

    def handle(self, msg):
        sender = msg['from']['id']
        chat = msg['chat']['id']
        if msg['chat']['type'] == 'private':
            self.bot.sendMessage(chat, "Я не поняла")
            self.bot.sendMessage(chat, f"А что значит \"{msg['text']}\"?")

    def connect(self):
        self.connection.connect(wait=True)
        self.connection.subscribe(destination="tg", id=1)

    def run_forever(self):
        self.connection.set_listener('', self)
        self.connect()
        self.bot.deleteWebhook()
        telepot.loop.MessageLoop(self.bot, self.handle).run_forever()

    def on_error(self, headers, message):
        _LOGGER.error('received an error: %s', message)

    def on_message(self, headers, message):
        _LOGGER.debug('received a message: %s', message)
        msg = json.loads(message)
        try:
            chat_id = msg['to']['chat_id']
            messages = msg['text']
        except KeyError:
            _LOGGER.error("Malformed message: %s", message)
            return
        _for_each(messages, partial(self.bot.sendMessage, chat_id))

    def on_disconnected(self):
        self.connect()
