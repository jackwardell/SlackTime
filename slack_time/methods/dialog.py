# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Dialog(SlackAPI):
    def open(self, dialog: str, trigger_id: str, **kwargs) -> Response:
        """
        Open a dialog with a user
        https://api.slack.com/methods/dialog.open

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param dialog: The dialog definition. This must be a JSON-encoded string.
        :type str:

        :param trigger_id: Exchange a trigger to post to the user.
        :type str: e.g. 12345.98765.abcd2358fdea

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.dialog.open(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "dialog": dialog, "trigger_id": trigger_id}

        return self._post("dialog.open", payload=payload, **kwargs)
