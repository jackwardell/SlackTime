# -*- coding: utf-8 -*-


def test_calls_add(slack_time):
    assert slack_time.calls.add


def test_calls_end(slack_time):
    assert slack_time.calls.end


def test_calls_info(slack_time):
    assert slack_time.calls.info


def test_calls_update(slack_time):
    assert slack_time.calls.update


def test_calls_participants_add(slack_time):
    assert slack_time.calls.participants.add


def test_calls_participants_remove(slack_time):
    assert slack_time.calls.participants.remove
