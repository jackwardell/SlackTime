# -*- coding: utf-8 -*-


def test_reminders_add(slack_time):
    assert slack_time.reminders.add


def test_reminders_complete(slack_time):
    assert slack_time.reminders.complete


def test_reminders_delete(slack_time):
    assert slack_time.reminders.delete


def test_reminders_info(slack_time):
    assert slack_time.reminders.info


def test_reminders_list(slack_time):
    assert slack_time.reminders.list
