# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Auth(SlackAPI):
    def revoke(self, test: bool = None, **kwargs) -> Response:
        """
        Revokes a token.
        https://api.slack.com/methods/auth.revoke

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param test: Setting this parameter to 1 triggers a testing mode where the specified token will not actually be revoked.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.auth.revoke(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "revoked": true
        }
        """

        payload = {"token": self._token}

        if test is not None:
            payload["test"] = test

        return self._get("auth.revoke", payload=payload, **kwargs)

    def test(self, **kwargs) -> Response:
        """
        Checks authentication & identity.
        https://api.slack.com/methods/auth.test

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.auth.test(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "url": "https://subarachnoid.slack.com/",
            "team": "Subarachnoid Workspace",
            "user": "grace",
            "team_id": "T12345678",
            "user_id": "W12345678"
        }
        """

        payload = {"token": self._token}

        return self._post("auth.test", payload=payload, **kwargs)
