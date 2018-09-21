import unittest

from slack_logging.formatters import SlackLoggerFormatter


class TestSlackLoggerFormatterEq(unittest.TestCase):

    def test_equal_items(self):
        fmtr1 = SlackLoggerFormatter(fmt='fmtr')
        fmtr2 = SlackLoggerFormatter(fmt='fmtr')
        self.assertEqual(fmtr1, fmtr2)
        self.assertIsNot(fmtr1, fmtr2)

    def test_unequal_items(self):
        fmtr1 = SlackLoggerFormatter(fmt='fmtr1')
        fmtr2 = SlackLoggerFormatter(fmt='fmtr2')
        self.assertNotEqual(fmtr1, fmtr2)
        self.assertIsNot(fmtr1, fmtr2)
