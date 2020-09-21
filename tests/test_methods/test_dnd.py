# -*- coding: utf-8 -*-


def test_dnd_end_dnd(slack_time):
    assert slack_time.dnd.end_dnd


def test_dnd_end_snooze(slack_time):
    assert slack_time.dnd.end_snooze


def test_dnd_info(slack_time):
    assert slack_time.dnd.info


def test_dnd_set_snooze(slack_time):
    assert slack_time.dnd.set_snooze


def test_dnd_team_info(slack_time):
    assert slack_time.dnd.team_info
