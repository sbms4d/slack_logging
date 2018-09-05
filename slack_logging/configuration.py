#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging


from slack_logging.handlers import SlackLoggerHandler
from slack_logging.formatters import LevelEmojis, SlackLoggerFormatter


def configure_slack_logger(logger_name, channels=None):
    """
    build a logger with handlers for the configured channels

    :type logger_name: str|unicode
    :type channels: list[str|unicode]
    :rtype: logging.Logger
    """
    logger = logging.getLogger(logger_name)

    for (log_level, channel) in (channels or WebHooks.items()):

        channel_handler = SlackLoggerHandler(channel.level)
        channel_handler.setFormatter = SlackLoggerFormatter(channel.name)

        logger.addHandler(channel_handler)

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


class WebHooks(object):

    _hooks = {}

    @classmethod
    def get_hook_for_level(cls, log_level):
        return cls._hooks[log_level].webhook

    @classmethod
    def configure_channel(cls, channel):
        """add a channel by name (replaces existing channel)"""
        # noinspection PyProtectedMember
        cls._hooks[logging._checkLevel(channel.level)] = channel

    @classmethod
    def items(cls):
        return cls._hooks.items()


class Channel(object):

    def __init__(self, name, webhook, level=logging.NOTSET):
        self.name = name
        self.webhook = webhook
        self.level = level
