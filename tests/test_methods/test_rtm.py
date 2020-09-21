# -*- coding: utf-8 -*-


def test_rtm_connect(slack_time):
    assert slack_time.rtm.connect


def test_rtm_start(slack_time):
    assert slack_time.rtm.start
