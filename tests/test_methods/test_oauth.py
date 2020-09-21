# -*- coding: utf-8 -*-


def test_oauth_access(slack_time):
    assert slack_time.oauth.access


def test_oauth_token(slack_time):
    assert slack_time.oauth.token


def test_oauth_v2_access(slack_time):
    assert slack_time.oauth.v2.access
