# -*- coding: utf-8 -*-


def test_migration_exchange(slack_time):
    assert slack_time.migration.exchange
