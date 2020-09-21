# -*- coding: utf-8 -*-


def test_files_comments_delete(slack_time):
    assert slack_time.files.comments.delete


def test_files_delete(slack_time):
    assert slack_time.files.delete


def test_files_info(slack_time):
    assert slack_time.files.info


def test_files_list(slack_time):
    assert slack_time.files.list


def test_files_revoke_public_u_r_l(slack_time):
    assert slack_time.files.revoke_public_u_r_l


def test_files_shared_public_u_r_l(slack_time):
    assert slack_time.files.shared_public_u_r_l


def test_files_upload(slack_time):
    assert slack_time.files.upload


def test_files_remote_add(slack_time):
    assert slack_time.files.remote.add


def test_files_remote_info(slack_time):
    assert slack_time.files.remote.info


def test_files_remote_list(slack_time):
    assert slack_time.files.remote.list


def test_files_remote_remove(slack_time):
    assert slack_time.files.remote.remove


def test_files_remote_share(slack_time):
    assert slack_time.files.remote.share


def test_files_remote_update(slack_time):
    assert slack_time.files.remote.update
