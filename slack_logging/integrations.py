#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integrations (webhooks) for slack channels
"""
import logging


class WebHooks(object):

    _hooks = {}

    @classmethod
    def get_hook_for_level(cls, log_level):
        # noinspection PyProtectedMember
        return cls._hooks[logging._checkLevel(log_level)].webhook

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
