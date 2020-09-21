# -*- coding: utf-8 -*-


def test_search_all(slack_time):
    assert slack_time.search.all


def test_search_files(slack_time):
    assert slack_time.search.files


def test_search_messages(slack_time):
    assert slack_time.search.messages
