# -*- coding: utf-8 -*-
import os

from slack_time.api import SlackError
from slack_time.methods import SlackTime

__all__ = ["SlackTime", "SlackError", "get_slack_time"]


def get_slack_time(env_var: str = "SLACK_API_TOKEN", **kwargs) -> SlackTime:
    token = os.getenv(env_var)
    assert token, f"You must save a '{env_var}' environment variable"
    return SlackTime(token, **kwargs)
