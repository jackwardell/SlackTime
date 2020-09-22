# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property


class Participants(SlackAPI):
    def add(self, id: str, users: str, **kwargs) -> Response:
        """
        Registers new participants added to a Call.
        https://api.slack.com/methods/calls.participants.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param id: id returned by the calls.add method.
        :type str: e.g. R0E69JAIF

        :param users: The list of users to add as participants in the Call. Read more on how to specify users here.
        :type str: e.g. [{"slack_id": "U1H77"}, {"external_id": "54321678", "display_name": "External User", "avatar_url": "https://example.com/users/avatar1234.jpg"}]

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.calls.participants.add(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "id": id, "users": users}

        return self._post("calls.participants.add", payload=payload, **kwargs)

    def remove(self, id: str, users: str, **kwargs) -> Response:
        """
        Registers participants removed from a Call.
        https://api.slack.com/methods/calls.participants.remove

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param id: id returned by the calls.add method.
        :type str: e.g. R0E69JAIF

        :param users: The list of users to remove as participants in the Call. Read more on how to specify users here.
        :type str: e.g. [{"slack_id": "U1H77"}, {"external_id": "54321678", "display_name": "External User", "avatar_url": "https://example.com/users/avatar1234.jpg"}]

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.calls.participants.remove(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "id": id, "users": users}

        return self._post("calls.participants.remove", payload=payload, **kwargs)


class Calls(SlackAPI):
    @cached_property
    def participants(self) -> Participants:
        return Participants(**self.params)

    def add(
        self,
        external_unique_id: str,
        join_url: str,
        created_by: str = None,
        date_start: int = None,
        desktop_app_join_url: str = None,
        external_display_id: str = None,
        title: str = None,
        users: list = None,
        **kwargs
    ) -> Response:
        """
        Registers a new Call.
        https://api.slack.com/methods/calls.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param external_unique_id: An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service.
        :type str: e.g. 025169F6-E37A-4E62-BB54-7F93A0FC4C1F

        :param join_url: The URL required for a client to join the Call.
        :type str: e.g. https://example.com/calls/1234567890

        :param created_by: The valid Slack user ID of the user who created this Call. When this method is called with a user token, the created_by field is optional and defaults to the authed user of the token. Otherwise, the field is required.
        :type str: e.g. U1H77

        :param date_start: Call start time in UTC UNIX timestamp format
        :type int: e.g. 1562002086

        :param desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
        :type str: e.g. callapp://join/1234567890

        :param external_display_id: An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.
        :type str: e.g. 705-292-868

        :param title: The name of the Call.
        :type str: e.g. Kimpossible sync up

        :param users: The list of users to register as participants in the Call. Read more on how to specify users here.
        :type list: e.g. [{"slack_id": "U1H77"}, {"external_id": "54321678", "display_name": "External User", "avatar_url": "https://example.com/users/avatar1234.jpg"}]

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.calls.add(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "call": {
                "id": "R0E69JAIF",
                "date_start": 1562002086,
                "external_unique_id": "025169F6-E37A-4E62-BB54-7F93A0FC4C1F",
                "join_url": "https://example.com/calls/1234567890",
                "desktop_app_join_url": "callapp://join/1234567890",
                "external_display_id": "705-292-868",
                "title": "Kimpossible sync up",
                "users": [
                    {
                        "slack_id": "U0MQG83FD"
                    },
                    {
                        "external_id": "54321678",
                        "display_name": "Kim Possible",
                        "avatar_url": "https://callmebeepme.com/users/avatar1234.jpg"
                    }
                ]
            }
        }
        """

        payload = {
            "token": self._token,
            "external_unique_id": external_unique_id,
            "join_url": join_url,
        }

        if created_by is not None:
            payload["created_by"] = created_by

        if date_start is not None:
            payload["date_start"] = date_start

        if desktop_app_join_url is not None:
            payload["desktop_app_join_url"] = desktop_app_join_url

        if external_display_id is not None:
            payload["external_display_id"] = external_display_id

        if title is not None:
            payload["title"] = title

        if users is not None:
            payload["users"] = users

        return self._post("calls.add", payload=payload, **kwargs)

    def end(self, id: str, duration: int = None, **kwargs) -> Response:
        """
        Ends a Call.
        https://api.slack.com/methods/calls.end

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param id: id returned when registering the call using the calls.add method.
        :type str: e.g. R0E69JAIF

        :param duration: Call duration in seconds
        :type int: e.g. 1800

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.calls.end(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }

        """

        payload = {"token": self._token, "id": id}

        if duration is not None:
            payload["duration"] = duration

        return self._post("calls.end", payload=payload, **kwargs)

    def info(self, id: str, **kwargs) -> Response:
        """
        Returns information about a Call.
        https://api.slack.com/methods/calls.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param id: id of the Call returned by the calls.add method.
        :type str: e.g. R0E69JAIF

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.calls.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "call": {
                "id": "R0E69JAIF",
                "date_start": 1562002086,
                "external_unique_id": "025169F6-E37A-4E62-BB54-7F93A0FC4C1F",
                "join_url": "https://callmebeepme.com/calls/1234567890",
                "desktop_app_join_url": "callapp://join/1234567890",
                "external_display_id": "705-292-868",
                "title": "Kimpossible sync up",
                "users": [
                    {
                        "slack_id": "U0MQG83FD"
                    },
                    {
                        "external_id": "54321678",
                        "display_name": "Kim Possible",
                        "avatar_url": "https://callmebeepme.com/users/avatar1234.jpg"
                    }
                ]
            }
        }
        """

        payload = {"token": self._token, "id": id}

        return self._post("calls.info", payload=payload, **kwargs)

    def update(
        self,
        id: str,
        desktop_app_join_url: str = None,
        join_url: str = None,
        title: str = None,
        **kwargs
    ) -> Response:
        """
        Updates information about a Call.
        https://api.slack.com/methods/calls.update

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param id: id returned by the calls.add method.
        :type str: e.g. R0E69JAIF

        :param desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
        :type str: e.g. callapp://join/0987654321

        :param join_url: The URL required for a client to join the Call.
        :type str: e.g. https://example.com/calls/0987654321

        :param title: The name of the Call.
        :type str: e.g. Kimpossible sync up call

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.calls.update(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "call": {
                "id": "R0E69JAIF",
                "date_start": 1562002086,
                "external_unique_id": "025169F6-E37A-4E62-BB54-7F93A0FC4C1F",
                "join_url": "https://callmebeepme.com/calls/0987654321",
                "desktop_app_join_url": "callapp://join/0987654321",
                "external_display_id": "705-292-868",
                "title": "Kimpossible sync up",
                "users": [
                    {
                        "slack_id": "U0MQG83FD"
                    },
                    {
                        "external_id": "54321678",
                        "display_name": "Kim Possible",
                        "avatar_url": "https://callmebeepme.com/users/avatar1234.jpg"
                    }
                ]
            }
        }
        """

        payload = {"token": self._token, "id": id}

        if desktop_app_join_url is not None:
            payload["desktop_app_join_url"] = desktop_app_join_url

        if join_url is not None:
            payload["join_url"] = join_url

        if title is not None:
            payload["title"] = title

        return self._post("calls.update", payload=payload, **kwargs)
