# -*- coding: utf-8 -*-
import os

from slack_time.methods import SlackTime


def get_slack() -> SlackTime:
    token = os.getenv("SLACK_API_TOKEN")
    return SlackTime(token)
