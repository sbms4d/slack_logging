#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from slack_logging.formatters import LevelEmojis, SlackLoggerFormatter
from slack_logging.handlers import SlackLoggerHandler


def configure_slack_logger(logger_name):
    """
    build a logger with handlers for the configured channels

    :type logger_name: str|unicode
    :rtype: logging.Logger
    """
    logger = logging.getLogger(logger_name)

    handler = SlackLoggerHandler()
    handler.setFormatter(SlackLoggerFormatter())

    logger.addHandler(handler)

    return logger


def set_slack_message_format(fmt):
    """Sets the message format for the formatters"""
    SlackLoggerFormatter.BASE_FORMAT = fmt


def set_level_emoji(log_level, emoji):
    """
    Set the specifics of a slack message format (colour and emoji) for each log level
    :type log_level: str
    :param str emoji: a slack emoji string e.g. :joy:
    """
    if hasattr(LevelEmojis, log_level):
        setattr(LevelEmojis, log_level, emoji)
    else:
        raise ValueError('Unsupported log level {}'.format(log_level))
