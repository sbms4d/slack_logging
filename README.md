# Slack Logging 

The slack logging package provides an interface to send log messages to a suitably configured slack channel

slack_logging currently supports python2 and python3.

## Interface
The slack logging does not override the default python logging. 
It provides a simple interface to create a logger capable of writing messages to slack
```python
>>> import slack_logging
>>> logger = slack_logging.configure_slack_logger(logger_name='my-app-logger')
```

## Managing slack integrations
After creating and integrating a slack app with a channel, a webhook is provided. 
This webhook should be added to `slack_logging` before the logging handler will attempt to write to the channel:
```python
>>> import slack_logging
>>> channel = slack_logging.Channel('channel-1', 'https://slack.com/webhook/channel-1/')
>>> slack_logging.WebHooks.configure_channel(channel)
```

## Channels
When creating a `slack_logging.channel` instance, you have the option of providing a log level. 
If the log level is provided, the logging to the channel is restricted to that level. 
Any logging calls with a level different (higher or lower) than that level will not be logged.
If not level is provided, the logger will have the level of the handler.
configuring channels after handlers have been created will cause the handlers to send messages to the new channels.

## Handlers
The `slack-logging` python package simply provides a `SlackLoggerHandler` that with the `SlackLoggerFormatter` creates a json message sent using the requests library. 
The handler only supports simple text messages. 
Stubs are in place to support attachments.

## Error Levels
Only the default python error levels are fully supported. 
While other log levels can be set, by default they will not have full message format support.
To support a new log level, create the level as normal and assign it a name via `logging`

### Adding emojis/colours
```python
>>> import slack_logging
>>> slack_logging.set_level_emoji(log_level='MY_LOG_LEVEL', emoji=':joy:')
```
