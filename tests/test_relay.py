import json
import logging
import unittest
from unittest.mock import call, MagicMock, sentinel

from tg import Tg


class BaseRelayTest(unittest.TestCase):

    def setUp(self):
        self.bot = Tg(sentinel.token, sentinel.connection)
        self.mock_request = MagicMock()
        self.bot.bot._api_request = self.mock_request

    def assert_messages(self, chat_id, messages):
        calls = [call('sendMessage',
                      {'chat_id': chat_id, 'text': message})
                 for message in messages]
        self.assertEqual(self.mock_request.call_args_list, calls)


class StompRelayTest(BaseRelayTest):
    def test_mock(self):
        self.bot.bot.sendMessage(sentinel.chat_id, sentinel.msg)

        self.assert_messages(sentinel.chat_id, (sentinel.msg,))

    def test_stomp_single_message(self):
        self.bot.on_message(None, json.dumps({"to": {"chat_id": "chat"},
                                              "text": "hello, world"}))

        self.assert_messages("chat", ("hello, world",))

    def test_stomp_multiple_messages_at_once(self):
        self.bot.on_message(None, json.dumps({"to": {"chat_id": "chat"},
                                              "text": ["hello", "world"]}))

        self.assert_messages("chat", ("hello", "world"))

    def test_stomp_error(self):
        with self.assertLogs("tg", logging.DEBUG) as cm:
            self.bot.on_error(None, "error message")
        self.assertEqual(cm.output, [f"ERROR:tg:received an error: error message"])


class MalformedMessagesTest(BaseRelayTest):
    def test_no_to(self):
        msg = json.dumps({"text": "hello, world"})
        with self.assertLogs("tg", logging.DEBUG) as cm:
            self.bot.on_message(None, msg)

        self.assertEqual(cm.output, [f"DEBUG:tg:received a message: {msg}",
                                     f"ERROR:tg:Malformed message: {msg}"])
        self.assert_messages(None, ())

    def test_no_chat_id(self):
        msg = json.dumps({"to": {}, "text": "hello, world"})
        with self.assertLogs("tg", logging.DEBUG) as cm:
            self.bot.on_message(None, msg)

        self.assertEqual(cm.output, [f"DEBUG:tg:received a message: {msg}",
                                     f"ERROR:tg:Malformed message: {msg}"])
        self.assert_messages(None, ())

    def test_no_message(self):
        msg = json.dumps({"to": {"chat_id": "1234"}})
        with self.assertLogs("tg", logging.DEBUG) as cm:
            self.bot.on_message(None, msg)

        self.assertEqual(cm.output, [f"DEBUG:tg:received a message: {msg}",
                                     f"ERROR:tg:Malformed message: {msg}"])
        self.assert_messages(None, ())
