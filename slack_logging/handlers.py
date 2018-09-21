#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import ujson

import requests

from slack_logging.integrations import WebHooks


class SlackLoggerHandler(logging.Handler):
    """
    Handler for the slack logger.
    Creates a Thread to send the slack message.
    Should be used with the formatter: SlackLoggerFormatter
    """

    def get_valid_webhooks(self, level):
        """
        Fetch the webhooks that should receive the log message
        :rtype: list[tuple[str,str]]
        """
        webhooks = [(c.webhook, c.name) for l, c in WebHooks.items() if not l or level == l]
        if not webhooks:
            raise RuntimeError('No Slack webhooks are configured!')
        return webhooks

    def emit(self, record):
        """
        If inheriting from logging.Handler you must overwrite the emit function.
        :param record: The logger record to be sent
        """
        try:
            formatted_record = self.format(record)

            for webhook, channel in self.get_valid_webhooks(record.levelno):

                payload = ujson.dumps({'text': formatted_record, 'username': record.name, 'channel': channel})

                requests.post(url=webhook, headers={'Content-Type': 'application/json'}, data=payload, timeout=5)

        except (KeyboardInterrupt, SystemExit):
            raise
        except (Exception, ):
            self.handleError(record)

    def __eq__(self, other):
        """Compare objects except the lock state (set to None for no comparison)"""
        return dict(self.__dict__, lock=None) == dict(other.__dict__, lock=None)
