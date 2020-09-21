# -*- coding: utf-8 -*-


def test_pins_add(slack_time):
    assert slack_time.pins.add


def test_pins_list(slack_time):
    assert slack_time.pins.list


def test_pins_remove(slack_time):
    assert slack_time.pins.remove
