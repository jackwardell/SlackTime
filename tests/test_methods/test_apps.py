# -*- coding: utf-8 -*-


def test_apps_permissions_info(slack_time):
    assert slack_time.apps.permissions.info


def test_apps_permissions_request(slack_time):
    assert slack_time.apps.permissions.request


def test_apps_permissions_resources_list(slack_time):
    assert slack_time.apps.permissions.resources.list


def test_apps_permissions_scopes_list(slack_time):
    assert slack_time.apps.permissions.scopes.list


def test_apps_permissions_users_list(slack_time):
    assert slack_time.apps.permissions.users.list


def test_apps_permissions_users_request(slack_time):
    assert slack_time.apps.permissions.users.request


def test_apps_uninstall(slack_time):
    assert slack_time.apps.uninstall
