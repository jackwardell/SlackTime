# -*- coding: utf-8 -*-


def test_workflows_step_completed(slack_time):
    assert slack_time.workflows.step_completed


def test_workflows_step_failed(slack_time):
    assert slack_time.workflows.step_failed


def test_workflows_update_step(slack_time):
    assert slack_time.workflows.update_step
