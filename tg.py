import json
import logging
from functools import partial

import stomp
import telepot
import telepot.loop


_LOGGER = logging.getLogger(__name__)
_CHANNEL = "tg"


def _for_each(maybe_list, func):
    if isinstance(maybe_list, list):
        for item in maybe_list:
            func(item)
    else:
        func(maybe_list)


def make_message(msg):
    _LOGGER.debug("Message:\n%s\n", msg)
    return json.dumps({"to": {"channel": "brain", "name": "niege"},
                       "from": {"channel": _CHANNEL,
                                "chat_id": msg['chat']['id'],
                                "user_id": msg['from']['id']},
                       "text": msg['text']})


class Tg(stomp.ConnectionListener):

    def __init__(self, token, conn):
        self.bot = telepot.Bot(token)
        self.connection = conn

    def handle(self, msg):
        if 'text' in msg:
            self.connection.send(body=make_message(msg), destination='brain')

    def connect(self):
        self.connection.connect(wait=True)
        self.connection.subscribe(destination=_CHANNEL, id=1)
        _LOGGER.info("Connected to stomp server")

    def run_forever(self):
        self.connection.set_listener('', self)
        self.connect()
        self.bot.deleteWebhook()
        telepot.loop.MessageLoop(self.bot, self.handle).run_forever()

    def on_error(self, headers, message):
        _LOGGER.error('received an error: %s', message)

    def on_message(self, headers, message):
        _LOGGER.debug('received a message: %s', message)
        try:
            msg = json.loads(message)
            chat_id = msg['to']['chat_id']
            messages = msg['text']
        except json.decoder.JSONDecodeError:
            _LOGGER.error("Malformed message (not json): %s", message)
            return
        except KeyError:
            _LOGGER.error("Malformed message: %s", message)
            return
        _for_each(messages, partial(self.bot.sendMessage, chat_id))

    def on_disconnected(self):
        _LOGGER.info("Connection to stomp server lost, reconnecting...")
        self.connect()
