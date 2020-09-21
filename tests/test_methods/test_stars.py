# -*- coding: utf-8 -*-


def test_stars_add(slack_time):
    assert slack_time.stars.add


def test_stars_list(slack_time):
    assert slack_time.stars.list


def test_stars_remove(slack_time):
    assert slack_time.stars.remove
