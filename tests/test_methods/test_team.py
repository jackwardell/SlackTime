# -*- coding: utf-8 -*-


def test_team_access_logs(slack_time):
    assert slack_time.team.access_logs


def test_team_billable_info(slack_time):
    assert slack_time.team.billable_info


def test_team_info(slack_time):
    assert slack_time.team.info


def test_team_integration_logs(slack_time):
    assert slack_time.team.integration_logs


def test_team_profile_get(slack_time):
    assert slack_time.team.profile.get
