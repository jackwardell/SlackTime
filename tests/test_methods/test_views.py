# -*- coding: utf-8 -*-


def test_views_open(slack_time):
    assert slack_time.views.open


def test_views_publish(slack_time):
    assert slack_time.views.publish


def test_views_push(slack_time):
    assert slack_time.views.push


def test_views_update(slack_time):
    assert slack_time.views.update
