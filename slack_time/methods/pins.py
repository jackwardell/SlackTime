# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Pins(SlackAPI):
    def add(self, channel: str, timestamp: float, **kwargs) -> Response:
        """
        Pins an item to a channel.
        https://api.slack.com/methods/pins.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel to pin the item in.
        :type str: e.g. C1234567890

        :param timestamp: Timestamp of the message to pin.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.pins.add(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel, "timestamp": timestamp}

        return self._post("pins.add", payload=payload, **kwargs)

    def list(self, channel: str, **kwargs) -> Response:
        """
        Lists items pinned to a channel.
        https://api.slack.com/methods/pins.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel to get pinned items for.
        :type str: e.g. C1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.pins.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "items": [
                {
                    "channel": "C2U86NC6H",
                    "created": 1508881078,
                    "created_by": "U2U85N1RZ",
                    "message": {
                        "permalink": "https://hitchhikers.slack.com/archives/C2U86NC6H/p1508197641000151",
                        "pinned_to": [
                            "C2U86NC6H"
                        ],
                        "text": "What is the meaning of life?",
                        "ts": "1508197641.000151",
                        "type": "message",
                        "user": "U2U85N1RZ"
                    },
                    "type": "message"
                },
                {
                    "channel": "C2U86NC6H",
                    "created": 1508880991,
                    "created_by": "U2U85N1RZ",
                    "message": {
                        "permalink": "https://hitchhikers.slack.com/archives/C2U86NC6H/p1508284197000015",
                        "pinned_to": [
                            "C2U86NC6H"
                        ],
                        "text": "The meaning of life, the universe, and everything is 42.",
                        "ts": "1503289197.000015",
                        "type": "message",
                        "user": "U2U85N1RZ"
                    },
                    "type": "message"
                }
            ],
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel}

        return self._get("pins.list", payload=payload, **kwargs)

    def remove(
        self,
        channel: str,
        file: str = None,
        file_comment: str = None,
        timestamp: float = None,
        **kwargs
    ) -> Response:
        """
        Un-pins an item from a channel.
        https://api.slack.com/methods/pins.remove

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel where the item is pinned to.
        :type str: e.g. C1234567890

        :param file: File to un-pin.
        :type str: e.g. F1234567890

        :param file_comment: File comment to un-pin.
        :type str: e.g. Fc1234567890

        :param timestamp: Timestamp of the message to un-pin.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.pins.remove(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel}

        if file is not None:
            payload["file"] = file

        if file_comment is not None:
            payload["file_comment"] = file_comment

        if timestamp is not None:
            payload["timestamp"] = timestamp

        return self._post("pins.remove", payload=payload, **kwargs)
