# -*- coding: utf-8 -*-


def test_admin_apps_approve(slack_time):
    assert slack_time.admin.apps.approve


def test_admin_apps_restrict(slack_time):
    assert slack_time.admin.apps.restrict


def test_admin_apps_approved_list(slack_time):
    assert slack_time.admin.apps.approved.list


def test_admin_apps_requests_list(slack_time):
    assert slack_time.admin.apps.requests.list


def test_admin_apps_restricted_list(slack_time):
    assert slack_time.admin.apps.restricted.list


def test_admin_conversations_archive(slack_time):
    assert slack_time.admin.conversations.archive


def test_admin_conversations_convert_to_private(slack_time):
    assert slack_time.admin.conversations.convert_to_private


def test_admin_conversations_create(slack_time):
    assert slack_time.admin.conversations.create


def test_admin_conversations_delete(slack_time):
    assert slack_time.admin.conversations.delete


def test_admin_conversations_disconnect_shared(slack_time):
    assert slack_time.admin.conversations.disconnect_shared


def test_admin_conversations_get_conversation_prefs(slack_time):
    assert slack_time.admin.conversations.get_conversation_prefs


def test_admin_conversations_get_teams(slack_time):
    assert slack_time.admin.conversations.get_teams


def test_admin_conversations_invite(slack_time):
    assert slack_time.admin.conversations.invite


def test_admin_conversations_rename(slack_time):
    assert slack_time.admin.conversations.rename


def test_admin_conversations_search(slack_time):
    assert slack_time.admin.conversations.search


def test_admin_conversations_set_conversation_prefs(slack_time):
    assert slack_time.admin.conversations.set_conversation_prefs


def test_admin_conversations_set_teams(slack_time):
    assert slack_time.admin.conversations.set_teams


def test_admin_conversations_unarchive(slack_time):
    assert slack_time.admin.conversations.unarchive


def test_admin_conversations_ekm_list_original_connected_channel_info(
    slack_time
):
    assert (
        slack_time.admin.conversations.ekm.list_original_connected_channel_info
    )


def test_admin_conversations_restrict_access_add_group(slack_time):
    assert slack_time.admin.conversations.restrict_access.add_group


def test_admin_conversations_restrict_access_list_groups(slack_time):
    assert slack_time.admin.conversations.restrict_access.list_groups


def test_admin_conversations_restrict_access_remove_group(slack_time):
    assert slack_time.admin.conversations.restrict_access.remove_group


def test_admin_emoji_add(slack_time):
    assert slack_time.admin.emoji.add


def test_admin_emoji_add_alias(slack_time):
    assert slack_time.admin.emoji.add_alias


def test_admin_emoji_list(slack_time):
    assert slack_time.admin.emoji.list


def test_admin_emoji_remove(slack_time):
    assert slack_time.admin.emoji.remove


def test_admin_emoji_rename(slack_time):
    assert slack_time.admin.emoji.rename


def test_admin_invite_requests_approve(slack_time):
    assert slack_time.admin.invite_requests.approve


def test_admin_invite_requests_deny(slack_time):
    assert slack_time.admin.invite_requests.deny


def test_admin_invite_requests_list(slack_time):
    assert slack_time.admin.invite_requests.list


def test_admin_invite_requests_approved_list(slack_time):
    assert slack_time.admin.invite_requests.approved.list


def test_admin_invite_requests_denied_list(slack_time):
    assert slack_time.admin.invite_requests.denied.list


def test_admin_teams_admins_list(slack_time):
    assert slack_time.admin.teams.admins.list


def test_admin_teams_create(slack_time):
    assert slack_time.admin.teams.create


def test_admin_teams_list(slack_time):
    assert slack_time.admin.teams.list


def test_admin_teams_owners_list(slack_time):
    assert slack_time.admin.teams.owners.list


def test_admin_teams_settings_info(slack_time):
    assert slack_time.admin.teams.settings.info


def test_admin_teams_settings_set_default_channels(slack_time):
    assert slack_time.admin.teams.settings.set_default_channels


def test_admin_teams_settings_set_description(slack_time):
    assert slack_time.admin.teams.settings.set_description


def test_admin_teams_settings_set_discoverability(slack_time):
    assert slack_time.admin.teams.settings.set_discoverability


def test_admin_teams_settings_set_icon(slack_time):
    assert slack_time.admin.teams.settings.set_icon


def test_admin_teams_settings_set_name(slack_time):
    assert slack_time.admin.teams.settings.set_name


def test_admin_usergroups_add_channels(slack_time):
    assert slack_time.admin.usergroups.add_channels


def test_admin_usergroups_add_teams(slack_time):
    assert slack_time.admin.usergroups.add_teams


def test_admin_usergroups_list_channels(slack_time):
    assert slack_time.admin.usergroups.list_channels


def test_admin_usergroups_remove_channels(slack_time):
    assert slack_time.admin.usergroups.remove_channels


def test_admin_users_assign(slack_time):
    assert slack_time.admin.users.assign


def test_admin_users_invite(slack_time):
    assert slack_time.admin.users.invite


def test_admin_users_list(slack_time):
    assert slack_time.admin.users.list


def test_admin_users_remove(slack_time):
    assert slack_time.admin.users.remove


def test_admin_users_set_admin(slack_time):
    assert slack_time.admin.users.set_admin


def test_admin_users_set_expiration(slack_time):
    assert slack_time.admin.users.set_expiration


def test_admin_users_set_owner(slack_time):
    assert slack_time.admin.users.set_owner


def test_admin_users_set_regular(slack_time):
    assert slack_time.admin.users.set_regular


def test_admin_users_session_reset(slack_time):
    assert slack_time.admin.users.session.reset
