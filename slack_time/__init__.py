# -*- coding: utf-8 -*-
import os

from slack_time.methods import SlackTime


def get_slack_time(env_var: str = "SLACK_API_TOKEN", **kwargs) -> SlackTime:
    token = os.getenv(env_var)
    assert token, "You must save a 'SLACK_API_TOKEN' environment variable"
    return SlackTime(token, **kwargs)
