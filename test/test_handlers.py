import unittest
import mock

from slack_logging.handlers import SlackLoggerHandler
from slack_logging import Channel


class TestGetValidWebhooks(unittest.TestCase):

    def test_webhooks(self):
        with mock.patch('slack_logging.handlers.WebHooks') as f:
            f.items.return_value = {0: Channel('', '', 0), 40: Channel('', '', 40)}.items()
            self.assertEqual(SlackLoggerHandler().get_valid_webhooks(10), [('', '')])
