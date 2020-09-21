# -*- coding: utf-8 -*-
import pytest
from slack_time import SlackTime


@pytest.fixture
def slack_time():
    return SlackTime("token")
