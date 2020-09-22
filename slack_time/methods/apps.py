# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property


class Resources(SlackAPI):
    def list(self, cursor: str = None, limit: int = None, **kwargs) -> Response:
        """
        Returns list of resource grants this app has on a team.
        https://api.slack.com/methods/apps.permissions.resources.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param limit: The maximum number of items to return.
        :type int: e.g. 20

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.apps.permissions.resources.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "resources": [
                {
                    "id": "T0DES3UAN",
                    "type": "team"
                },
                {
                    "id": "D024BFF1M",
                    "type": "app_home"
                },
                {
                    "id": "C024BE91L",
                    "type": "channel"
                }
            ],
            "response_metadata": {
                "next_cursor": "dGVhbTpDMUg5UkVTR0w="
            }
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._get("apps.permissions.resources.list", payload=payload, **kwargs)


class Scopes(SlackAPI):
    def list(self, **kwargs) -> Response:
        """
        Returns list of scopes this app has on a team.
        https://api.slack.com/methods/apps.permissions.scopes.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.apps.permissions.scopes.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "scopes": {
                "app_home": [
                    "chat:write",
                    "im:history",
                    "im:read"
                ],
                "team": [
                    "users:read"
                ],
                "channel": [
                    "channels:history",
                    "chat:write"
                ],
                "group": [
                    "chat:write"
                ],
                "mpim": [
                    "chat:write"
                ],
                "im": [
                    "chat:write"
                ],
                "user": []
            }
        }
        """

        payload = {"token": self._token}

        return self._get("apps.permissions.scopes.list", payload=payload, **kwargs)


class Users(SlackAPI):
    def list(self, cursor: str = None, limit: int = None, **kwargs) -> Response:
        """
        Returns list of user grants and corresponding scopes this app has on a team.
        https://api.slack.com/methods/apps.permissions.users.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param limit: The maximum number of items to return.
        :type int: e.g. 20

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.apps.permissions.users.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "resources": [
                {
                    "id": "U0DES3UAN",
                    "scopes": [
                        "dnd:write:user",
                        "reminders:write:user"
                    ]
                },
                {
                    "id": "U024BFF1M",
                    "scopes": [
                        "reminders:write:user"
                    ]
                }
            ],
            "response_metadata": {
                "next_cursor": "dGVhbTdPMUg5UkFTT0w="
            }
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._get("apps.permissions.users.list", payload=payload, **kwargs)

    def request(self, scopes: str, trigger_id: str, user: str, **kwargs) -> Response:
        """
        Enables an app to trigger a permissions modal to grant an app access to a user access scope.
        https://api.slack.com/methods/apps.permissions.users.request

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param scopes: A comma separated list of user scopes to request for
        :type str:

        :param trigger_id: Token used to trigger the request
        :type str:

        :param user: The user this scope is being requested for
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.apps.permissions.users.request(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "scopes": scopes,
            "trigger_id": trigger_id,
            "user": user,
        }

        return self._get("apps.permissions.users.request", payload=payload, **kwargs)


class Permissions(SlackAPI):
    def info(self, **kwargs) -> Response:
        """
        Returns list of permissions this app has on a team.
        https://api.slack.com/methods/apps.permissions.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.apps.permissions.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "info": {
                "team": {
                    "scopes": [],
                    "resources": {
                        "ids": []
                    }
                },
                "channel": {
                    "scopes": [
                        "channels:read"
                    ],
                    "resources": {
                        "ids": [
                            "C061FA5PB"
                        ],
                        "wildcard": false,
                        "excluded_ids": []
                    }
                },
                "group": {
                    "scopes": [],
                    "resources": {
                        "ids": []
                    }
                },
                "mpim": {
                    "scopes": [],
                    "resources": {
                        "ids": []
                    }
                },
                "im": {
                    "scopes": [],
                    "resources": {
                        "ids": []
                    }
                },
                "app_home": {
                    "scopes": [
                        "chat:write",
                        "im:history",
                        "im:read"
                    ],
                    "resources": {
                        "ids": [
                            "D0C0NU1Q8",
                            "D0BH95DLH"
                        ]
                    }
                }
            }
        }
        """

        payload = {"token": self._token}

        return self._get("apps.permissions.info", payload=payload, **kwargs)

    def request(self, scopes: str, trigger_id: str, **kwargs) -> Response:
        """
        Allows an app to request additional scopes
        https://api.slack.com/methods/apps.permissions.request

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param scopes: A comma separated list of scopes to request for
        :type str:

        :param trigger_id: Token used to trigger the permissions API
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.apps.permissions.request(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "scopes": scopes, "trigger_id": trigger_id}

        return self._get("apps.permissions.request", payload=payload, **kwargs)

    @cached_property
    def resources(self) -> Resources:
        return Resources(**self.params)

    @cached_property
    def scopes(self):
        return Scopes(**self.params)

    @cached_property
    def users(self) -> Users:
        return Users(**self.params)


class Apps(SlackAPI):
    @cached_property
    def permissions(self) -> Permissions:
        return Permissions(**self.params)

    def uninstall(self, client_id: float, client_secret: str, **kwargs) -> Response:
        """
        Uninstalls your app from a workspace.
        https://api.slack.com/methods/apps.uninstall

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param client_id: Issued when you created your application.
        :type float: e.g. 56579136444.26251006572

        :param client_secret: Issued when you created your application.
        :type str: e.g. f25b5ceaf8a3c2a2c4f52bb4f0b0499e

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.apps.uninstall(**your_params)
        <Response [200]>
        """

        payload = {
            "token": self._token,
            "client_id": client_id,
            "client_secret": client_secret,
        }

        return self._get("apps.uninstall", payload=payload, **kwargs)
