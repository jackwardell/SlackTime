# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property


class V2(SlackAPI):
    def access(
        self,
        code: str,
        client_id: str = None,
        client_secret: str = None,
        redirect_uri: str = None,
        **kwargs
    ) -> Response:
        """
        Exchanges a temporary OAuth verifier code for an access token.
        https://api.slack.com/methods/oauth.v2.access

        :param code: The code param returned via the OAuth callback.
        :type str: e.g. ccdaa72ad

        :param client_id: Issued when you created your application.
        :type str: e.g. 4b39e9-752c4

        :param client_secret: Issued when you created your application.
        :type str: e.g. 33fea0113f5b1

        :param redirect_uri: This must match the originally submitted URI (if one was sent).
        :type str: e.g. http://example.com

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.oauth.v2.access(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "access_token": "xoxb-17653672481-19874698323-pdFZKVeTuE8sk7oOcBrzbqgy",
            "token_type": "bot",
            "scope": "commands,incoming-webhook",
            "bot_user_id": "U0KRQLJ9H",
            "app_id": "A0KRD7HC3",
            "team": {
                "name": "Slack Softball Team",
                "id": "T9TK3CUKW"
            },
            "enterprise": {
                "name": "slack-sports",
                "id": "E12345678"
            },
            "authed_user": {
                "id": "U1234",
                "scope": "chat:write",
                "access_token": "xoxp-1234",
                "token_type": "user"
            }
        }
        """

        payload = {"token": self._token, "code": code}

        if client_id is not None:
            payload["client_id"] = client_id

        if client_secret is not None:
            payload["client_secret"] = client_secret

        if redirect_uri is not None:
            payload["redirect_uri"] = redirect_uri

        return self._post("oauth.v2.access", payload=payload, **kwargs)


class OAuth(SlackAPI):
    @cached_property
    def v2(self) -> V2:
        return V2(**self.params)

    def access(
        self,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        redirect_uri: str = None,
        single_channel: bool = None,
        **kwargs
    ) -> Response:
        """
        Exchanges a temporary OAuth verifier code for an access token.
        https://api.slack.com/methods/oauth.access

        A potential gotcha: while redirect_uri is optional, it is required if your app passed it as a parameter to oauth/authorization in the first step of the OAuth flow.

        :param client_id: Issued when you created your application.
        :type str: e.g. 4b39e9-752c4

        :param client_secret: Issued when you created your application.
        :type str: e.g. 33fea0113f5b1

        :param code: The code param returned via the OAuth callback.
        :type str: e.g. ccdaa72ad

        :param redirect_uri: This must match the originally submitted URI (if one was sent).
        :type str: e.g. http://example.com

        :param single_channel: Request the user to add your app only to a single channel. Only valid with a legacy workspace app.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.oauth.access(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "access_token": "xoxp-XXXXXXXX-XXXXXXXX-XXXXX",
            "scope": "groups:write",
            "team_name": "Wyld Stallyns LLC",
            "team_id": "TXXXXXXXXX",
            "enterprise_id": null
        }
        """

        payload = {"token": self._token}

        if client_id is not None:
            payload["client_id"] = client_id

        if client_secret is not None:
            payload["client_secret"] = client_secret

        if code is not None:
            payload["code"] = code

        if redirect_uri is not None:
            payload["redirect_uri"] = redirect_uri

        if single_channel is not None:
            payload["single_channel"] = single_channel

        return self._post("oauth.access", payload=payload, **kwargs)

    def token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str = None,
        single_channel: bool = None,
        **kwargs
    ) -> Response:
        """
        Exchanges a temporary OAuth verifier code for a workspace token.
        https://api.slack.com/methods/oauth.token

        :param client_id: Issued when you created your application.
        :type str: e.g. 4b39e9-752c4

        :param client_secret: Issued when you created your application.
        :type str: e.g. 33fea0113f5b1

        :param code: The code param returned via the OAuth callback.
        :type str: e.g. ccdaa72ad

        :param redirect_uri: This must match the originally submitted URI (if one was sent).
        :type str: e.g. http://example.com

        :param single_channel: Request the user to add your app only to a single channel.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.oauth.token(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "access_token": "xoxa-access-token-string",
            "token_type": "app",
            "app_id": "A012345678",
            "app_user_id": "U0AB12ABC",
            "installer_user_id": "U061F7AUR",
            "authorizing_user_id": "U0HTT3Q0G",
            "team_name": "Subarachnoid Workspace",
            "team_id": "T061EG9Z9",
            "permissions": [
                {
                    "scopes": [
                        "channels:read",
                        "chat:write:user"
                    ],
                    "resource_type": "channel",
                    "resource_id": 0
                }
            ],
            "single_channel_id": "C061EG9T2"
        }
        """

        payload = {
            "token": self._token,
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
        }

        if redirect_uri is not None:
            payload["redirect_uri"] = redirect_uri

        if single_channel is not None:
            payload["single_channel"] = single_channel

        return self._post("oauth.token", payload=payload, **kwargs)
