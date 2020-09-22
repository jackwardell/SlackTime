# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Reactions(SlackAPI):
    def add(self, channel: str, name: str, timestamp: float, **kwargs) -> Response:
        """
        Adds a reaction to an item.
        https://api.slack.com/methods/reactions.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel where the message to add reaction to was posted.
        :type str: e.g. C1234567890

        :param name: Reaction (emoji) name.
        :type str: e.g. thumbsup

        :param timestamp: Timestamp of the message to add reaction to.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reactions.add(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "channel": channel,
            "name": name,
            "timestamp": timestamp,
        }

        return self._post("reactions.add", payload=payload, **kwargs)

    def get(
        self,
        channel: str = None,
        file: str = None,
        file_comment: str = None,
        full: bool = None,
        timestamp: float = None,
        **kwargs
    ) -> Response:
        """
        Gets reactions for an item.
        https://api.slack.com/methods/reactions.get

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel where the message to get reactions for was posted.
        :type str: e.g. C1234567890

        :param file: File to get reactions for.
        :type str: e.g. F1234567890

        :param file_comment: File comment to get reactions for.
        :type str: e.g. Fc1234567890

        :param full: If true always return the complete reaction list.
        :type bool: e.g. true

        :param timestamp: Timestamp of the message to get reactions for.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reactions.get(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "file": {
                "channels": [
                    "C2U7V2YA2"
                ],
                "comments_count": 1,
                "created": 1507850315,
                "groups": [],
                "id": "F7H0D7ZA4",
                "ims": [],
                "name": "computer.gif",
                "reactions": [
                    {
                        "count": 1,
                        "name": "stuck_out_tongue_winking_eye",
                        "users": [
                            "U2U85N1RV"
                        ]
                    }
                ],
                "timestamp": 1507850315,
                "title": "computer.gif",
                "user": "U2U85N1RV"
            },
            "ok": true,
            "type": "file"
        }
        """

        payload = {"token": self._token}

        if channel is not None:
            payload["channel"] = channel

        if file is not None:
            payload["file"] = file

        if file_comment is not None:
            payload["file_comment"] = file_comment

        if full is not None:
            payload["full"] = full

        if timestamp is not None:
            payload["timestamp"] = timestamp

        return self._get("reactions.get", payload=payload, **kwargs)

    def list(
        self,
        count: int = None,
        cursor: str = None,
        full: bool = None,
        limit: int = None,
        page: int = None,
        user: str = None,
        **kwargs
    ) -> Response:
        """
        Lists reactions made by a user.
        https://api.slack.com/methods/reactions.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param count: Number of items to return per page.
        :type int: e.g. 20

        :param cursor: Parameter for pagination. Set cursor equal to the next_cursor attribute returned by the previous request's response_metadata. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection. See pagination for more details.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param full: If true always return the complete reaction list.
        :type bool: e.g. true

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
        :type int: e.g. 20

        :param page: Page number of results to return.
        :type int: e.g. 2

        :param user: Show reactions made by this user. Defaults to the authed user.
        :type str: e.g. W1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reactions.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "items": [
                {
                    "type": "message",
                    "channel": "C3UKJTQAC",
                    "message": {
                        "bot_id": "B4VLRLMKJ",
                        "reactions": [
                            {
                                "count": 1,
                                "name": "robot_face",
                                "users": [
                                    "U2U85N1RV"
                                ]
                            }
                        ],
                        "subtype": "bot_message",
                        "text": "Hello from Python! :tada:",
                        "ts": "1507849573.000090",
                        "username": "Shipit Notifications"
                    }
                },
                {
                    "comment": {
                        "type": "file_comment",
                        "comment": "This is a file comment",
                        "created": 1508286096,
                        "id": "Fc7LP08P1U",
                        "reactions": [
                            {
                                "count": 1,
                                "name": "white_check_mark",
                                "users": [
                                    "U2U85N1RV"
                                ]
                            }
                        ],
                        "timestamp": 1508286096,
                        "user": "U2U85N1RV"
                    },
                    "file": {
                        "channels": [
                            "C2U7V2YA2"
                        ],
                        "comments_count": 1,
                        "created": 1507850315,
                        "reactions": [
                            {
                                "count": 1,
                                "name": "stuck_out_tongue_winking_eye",
                                "users": [
                                    "U2U85N1RV"
                                ]
                            }
                        ],
                        "title": "computer.gif",
                        "user": "U2U85N1RV",
                        "username": ""
                    }
                },
                {
                    "file": {
                        "channels": [
                            "C2U7V2YA2"
                        ],
                        "comments_count": 1,
                        "created": 1507850315,
                        "id": "F7H0D7ZA4",
                        "name": "computer.gif",
                        "reactions": [
                            {
                                "count": 1,
                                "name": "stuck_out_tongue_winking_eye",
                                "users": [
                                    "U2U85N1RV"
                                ]
                            }
                        ],
                        "size": 1639034,
                        "title": "computer.gif",
                        "user": "U2U85N1RV",
                        "username": ""
                    },
                    "type": "file"
                }
            ],
            "ok": true,
            "response_metadata": {
                "next_cursor": "dGVhbTpDMUg5UkVTR0w="
            }
        }
        """

        payload = {"token": self._token}

        if count is not None:
            payload["count"] = count

        if cursor is not None:
            payload["cursor"] = cursor

        if full is not None:
            payload["full"] = full

        if limit is not None:
            payload["limit"] = limit

        if page is not None:
            payload["page"] = page

        if user is not None:
            payload["user"] = user

        return self._get("reactions.list", payload=payload, **kwargs)

    def remove(
        self,
        name: str,
        channel: str = None,
        file: str = None,
        file_comment: str = None,
        timestamp: float = None,
        **kwargs
    ) -> Response:
        """
        Removes a reaction from an item.
        https://api.slack.com/methods/reactions.remove

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: Reaction (emoji) name.
        :type str: e.g. thumbsup

        :param channel: Channel where the message to remove reaction from was posted.
        :type str: e.g. C1234567890

        :param file: File to remove reaction from.
        :type str: e.g. F1234567890

        :param file_comment: File comment to remove reaction from.
        :type str: e.g. Fc1234567890

        :param timestamp: Timestamp of the message to remove reaction from.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reactions.remove(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "name": name}

        if channel is not None:
            payload["channel"] = channel

        if file is not None:
            payload["file"] = file

        if file_comment is not None:
            payload["file_comment"] = file_comment

        if timestamp is not None:
            payload["timestamp"] = timestamp

        return self._post("reactions.remove", payload=payload, **kwargs)
