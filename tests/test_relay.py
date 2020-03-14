import unittest
from unittest.mock import MagicMock, sentinel

from tg import Tg


class RelayTest(unittest.TestCase):

    def setUp(self):
        self.bot = Tg(sentinel.token, sentinel.connection)
        self.mock_request = MagicMock()
        self.bot.bot._api_request = self.mock_request

    def test_mock(self):
        self.bot.bot.sendMessage(sentinel.chat_id, sentinel.msg)
        self.mock_request.assert_called_once_with('sendMessage',
                                                  {'chat_id': sentinel.chat_id,
                                                   'text': sentinel.msg})
