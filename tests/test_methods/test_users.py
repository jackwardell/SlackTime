# -*- coding: utf-8 -*-


def test_users_conversations(slack_time):
    assert slack_time.users.conversations


def test_users_delete_photo(slack_time):
    assert slack_time.users.delete_photo


def test_users_get_presence(slack_time):
    assert slack_time.users.get_presence


def test_users_identity(slack_time):
    assert slack_time.users.identity


def test_users_info(slack_time):
    assert slack_time.users.info


def test_users_list(slack_time):
    assert slack_time.users.list


def test_users_lookup_by_email(slack_time):
    assert slack_time.users.lookup_by_email


def test_users_set_active(slack_time):
    assert slack_time.users.set_active


def test_users_set_photo(slack_time):
    assert slack_time.users.set_photo


def test_users_set_presence(slack_time):
    assert slack_time.users.set_presence


def test_users_profile_get(slack_time):
    assert slack_time.users.profile.get


def test_users_profile_set(slack_time):
    assert slack_time.users.profile.set
