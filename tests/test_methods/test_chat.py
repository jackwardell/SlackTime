# -*- coding: utf-8 -*-


def test_chat_delete(slack_time):
    assert slack_time.chat.delete


def test_chat_delete_scheduled_message(slack_time):
    assert slack_time.chat.delete_scheduled_message


def test_chat_get_permalink(slack_time):
    assert slack_time.chat.get_permalink


def test_chat_me_message(slack_time):
    assert slack_time.chat.me_message


def test_chat_post_ephemeral(slack_time):
    assert slack_time.chat.post_ephemeral


def test_chat_post_message(slack_time):
    assert slack_time.chat.post_message


def test_chat_schedule_message(slack_time):
    assert slack_time.chat.schedule_message


def test_chat_unfurl(slack_time):
    assert slack_time.chat.unfurl


def test_chat_update(slack_time):
    assert slack_time.chat.update


def test_chat_scheduled_messages_list(slack_time):
    assert slack_time.chat.scheduled_messages.list
