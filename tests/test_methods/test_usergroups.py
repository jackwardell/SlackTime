# -*- coding: utf-8 -*-


def test_usergroups_create(slack_time):
    assert slack_time.usergroups.create


def test_usergroups_disable(slack_time):
    assert slack_time.usergroups.disable


def test_usergroups_enable(slack_time):
    assert slack_time.usergroups.enable


def test_usergroups_list(slack_time):
    assert slack_time.usergroups.list


def test_usergroups_update(slack_time):
    assert slack_time.usergroups.update


def test_usergroups_users_list(slack_time):
    assert slack_time.usergroups.users.list


def test_usergroups_users_update(slack_time):
    assert slack_time.usergroups.users.update
