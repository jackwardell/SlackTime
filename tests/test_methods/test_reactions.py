# -*- coding: utf-8 -*-


def test_reactions_add(slack_time):
    assert slack_time.reactions.add


def test_reactions_get(slack_time):
    assert slack_time.reactions.get


def test_reactions_list(slack_time):
    assert slack_time.reactions.list


def test_reactions_remove(slack_time):
    assert slack_time.reactions.remove
