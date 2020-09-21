# -*- coding: utf-8 -*-


def test_conversations_archive(slack_time):
    assert slack_time.conversations.archive


def test_conversations_close(slack_time):
    assert slack_time.conversations.close


def test_conversations_create(slack_time):
    assert slack_time.conversations.create


def test_conversations_history(slack_time):
    assert slack_time.conversations.history


def test_conversations_info(slack_time):
    assert slack_time.conversations.info


def test_conversations_invite(slack_time):
    assert slack_time.conversations.invite


def test_conversations_join(slack_time):
    assert slack_time.conversations.join


def test_conversations_kick(slack_time):
    assert slack_time.conversations.kick


def test_conversations_leave(slack_time):
    assert slack_time.conversations.leave


def test_conversations_list(slack_time):
    assert slack_time.conversations.list


def test_conversations_mark(slack_time):
    assert slack_time.conversations.mark


def test_conversations_members(slack_time):
    assert slack_time.conversations.members


def test_conversations_open(slack_time):
    assert slack_time.conversations.open


def test_conversations_rename(slack_time):
    assert slack_time.conversations.rename


def test_conversations_replies(slack_time):
    assert slack_time.conversations.replies


def test_conversations_set_purpose(slack_time):
    assert slack_time.conversations.set_purpose


def test_conversations_set_topic(slack_time):
    assert slack_time.conversations.set_topic


def test_conversations_unarchive(slack_time):
    assert slack_time.conversations.unarchive
