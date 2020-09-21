# -*- coding: utf-8 -*-


def test_auth_revoke(slack_time):
    assert slack_time.auth.revoke


def test_auth_test(slack_time):
    assert slack_time.auth.test
