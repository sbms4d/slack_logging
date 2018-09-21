import unittest

from slack_logging.configuration import configure_slack_logger, logging


class TestConfigureSlackLogger(unittest.TestCase):

    def test_return_type(self):
        self.assertEqual(isinstance(configure_slack_logger(''), logging.getLoggerClass()), True)
