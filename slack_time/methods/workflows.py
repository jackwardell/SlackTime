# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Workflows(SlackAPI):
    def step_completed(
        self, workflow_step_execute_id: dict, outputs: dict = None, **kwargs
    ) -> Response:
        """
        Indicate that an app's step in a workflow completed execution.
        https://api.slack.com/methods/workflows.stepCompleted

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
        :type dict:

        :param outputs: Key-value object of outputs from your step. Keys of this object reflect the configured key properties of your outputs array from your workflow_step object.
        :type dict:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.workflows.step_completed(**your_params)
        <Response [200]>
        """

        payload = {
            "token": self._token,
            "workflow_step_execute_id": workflow_step_execute_id,
        }

        if outputs is not None:
            payload["outputs"] = outputs

        return self._post("workflows.stepCompleted", payload=payload, **kwargs)

    def step_failed(
        self, error: str, workflow_step_execute_id: str, **kwargs
    ) -> Response:
        """
        Indicate that an app's step in a workflow failed to execute.
        https://api.slack.com/methods/workflows.stepFailed

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param error: A JSON-based object with a message property that should contain a human readable error message.
        :type dict:

        :param workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
        :type dict:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.workflows.step_failed(**your_params)
        <Response [200]>
        """

        payload = {
            "token": self._token,
            "error": error,
            "workflow_step_execute_id": workflow_step_execute_id,
        }

        return self._post("workflows.stepFailed", payload=payload, **kwargs)

    def update_step(
        self,
        workflow_step_edit_id: str,
        inputs: dict = None,
        outputs: list = None,
        **kwargs
    ) -> Response:
        """
        Update the configuration for a workflow extension step.
        https://api.slack.com/methods/workflows.updateStep

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param workflow_step_edit_id: A context identifier provided with view_submission payloads used to call back to workflows.updateStep.
        :type str:

        :param inputs: A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts.
        :type dict: e.g. {"title":{"value":"The Title"},"submitter":{"value":"{{user}}"}}

        :param outputs: An JSON array of output objects used during step execution. This is the data your app agrees to provide when your workflow step was executed.
        :type list: e.g. [{"name":"ticket_id","type":"text","label":"Ticket ID"},{"name":"title","type":"text","label":"Title"}]

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.workflows.update_step(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "workflow_step_edit_id": workflow_step_edit_id}

        if inputs is not None:
            payload["inputs"] = inputs

        if outputs is not None:
            payload["outputs"] = outputs

        return self._post("workflows.updateStep", payload=payload, **kwargs)
