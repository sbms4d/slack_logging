#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging


class LevelEmojis(object):

    CRITICAL = ':skull_and_crossbones:'
    ERROR = ':fire:'
    WARNING = ':warning:'
    INFO = ':information_source:'
    DEBUG = ':hammer_and_wrench:'
    NOTSET = ':question:'

    @classmethod
    def get(cls, level):
        """
        Get the emoji that represents this logging level.
        Defaults to warning if no level can be found in the loopup
        :param str level: The log level. e.g. INFO or ERROR
        :return: The emoji for this logging level
        :rtype: str
        """
        return getattr(cls, level, ':warning:')


class SlackLoggerFormatter(logging.Formatter):
    """
    The slack logger formatter.
    """
    BASE_FORMAT = '{emoji} {level} - {name}: \n{message}'

    def format(self, record):
        """
        The formatter that overwrites the base logger class formatter.
        This is used to format the message into a slack recognised message.
        :param record: The logger record
        :return: A string subject to slack formatting
        :rtype: str
        """
        level = record.levelname
        message = super(SlackLoggerFormatter, self).format(record)
        emoji = LevelEmojis.get(level)

        text = self.BASE_FORMAT.format(emoji=emoji, level=level.title(), name=record.name, message=message)

        return text

    def __eq__(self, other):
        """Python3 formatters are non-equivalent given the same __init__ parameters"""
        return dict(self.__dict__, _style=None) == dict(other.__dict__, _style=None)
