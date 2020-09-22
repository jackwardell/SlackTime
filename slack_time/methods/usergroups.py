# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property


class Users(SlackAPI):
    def list(self, usergroup: str, include_disabled: bool = None, **kwargs) -> Response:
        """
        List all users in a User Group
        https://api.slack.com/methods/usergroups.users.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param usergroup: The encoded ID of the User Group to update.
        :type str: e.g. S0604QSJC

        :param include_disabled: Allow results that involve disabled User Groups.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.usergroups.users.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "users": [
                "U060R4BJ4",
                "W123A4BC5"
            ]
        }
        """

        payload = {"token": self._token, "usergroup": usergroup}

        if include_disabled is not None:
            payload["include_disabled"] = include_disabled

        return self._get("usergroups.users.list", payload=payload, **kwargs)

    def update(
        self, usergroup: str, users: str, include_count: bool = None, **kwargs
    ) -> Response:
        """
        Update the list of users for a User Group
        https://api.slack.com/methods/usergroups.users.update

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param usergroup: The encoded ID of the User Group to update.
        :type str: e.g. S0604QSJC

        :param users: A comma separated string of encoded user IDs that represent the entire list of users for the User Group.
        :type str: e.g. U060R4BJ4,U060RNRCZ

        :param include_count: Include the number of users in the User Group.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.usergroups.users.update(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "usergroup": {
                "id": "S0616NG6M",
                "team_id": "T060R4BHN",
                "is_usergroup": true,
                "name": "Marketing Team",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1447096577,
                "date_update": 1447102109,
                "date_delete": 0,
                "auto_type": null,
                "created_by": "U060R4BJ4",
                "updated_by": "U060R4BJ4",
                "deleted_by": null,
                "prefs": {
                    "channels": [],
                    "groups": []
                },
                "users": [
                    "U060R4BJ4",
                    "U060RNRCZ"
                ],
                "user_count": 1
            }
        }
        """

        payload = {"token": self._token, "usergroup": usergroup, "users": users}

        if include_count is not None:
            payload["include_count"] = include_count

        return self._post("usergroups.users.update", payload=payload, **kwargs)


class Usergroups(SlackAPI):
    @cached_property
    def users(self) -> Users:
        return Users(**self.params)

    def create(
        self,
        name: str,
        channels: str = None,
        description: str = None,
        handle: str = None,
        include_count: bool = None,
        **kwargs
    ) -> Response:
        """
        Create a User Group
        https://api.slack.com/methods/usergroups.create

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: A name for the User Group. Must be unique among User Groups.
        :type str: e.g. My Test Team

        :param channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
        :type str: e.g. C1234567890,C2345678901,C3456789012

        :param description: A short description of the User Group.
        :type str:

        :param handle: A mention handle. Must be unique among channels, users and User Groups.
        :type str: e.g. marketing

        :param include_count: Include the number of users in each User Group.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.usergroups.create(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "name": name}

        if channels is not None:
            payload["channels"] = channels

        if description is not None:
            payload["description"] = description

        if handle is not None:
            payload["handle"] = handle

        if include_count is not None:
            payload["include_count"] = include_count

        return self._post("usergroups.create", payload=payload, **kwargs)

    def disable(self, usergroup: str, include_count: bool = None, **kwargs) -> Response:
        """
        Disable an existing User Group
        https://api.slack.com/methods/usergroups.disable

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param usergroup: The encoded ID of the User Group to disable.
        :type str: e.g. S0604QSJC

        :param include_count: Include the number of users in the User Group.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.usergroups.disable(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "usergroup": usergroup}

        if include_count is not None:
            payload["include_count"] = include_count

        return self._post("usergroups.disable", payload=payload, **kwargs)

    def enable(self, usergroup: str, include_count: bool = None, **kwargs) -> Response:
        """
        Enable a User Group
        https://api.slack.com/methods/usergroups.enable

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param usergroup: The encoded ID of the User Group to enable.
        :type str: e.g. S0604QSJC

        :param include_count: Include the number of users in the User Group.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.usergroups.enable(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "usergroup": usergroup}

        if include_count is not None:
            payload["include_count"] = include_count

        return self._post("usergroups.enable", payload=payload, **kwargs)

    def list(
        self,
        include_count: bool = None,
        include_disabled: bool = None,
        include_users: bool = None,
        **kwargs
    ) -> Response:
        """
        List all User Groups for a team
        https://api.slack.com/methods/usergroups.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param include_count: Include the number of users in each User Group.
        :type bool: e.g. true

        :param include_disabled: Include disabled User Groups.
        :type bool: e.g. true

        :param include_users: Include the list of users for each User Group.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.usergroups.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "usergroups": [
                {
                    "id": "S0614TZR7",
                    "team_id": "T060RNRCH",
                    "is_usergroup": true,
                    "name": "Team Admins",
                    "description": "A group of all Administrators on your team.",
                    "handle": "admins",
                    "is_external": false,
                    "date_create": 1446598059,
                    "date_update": 1446670362,
                    "date_delete": 0,
                    "auto_type": "admin",
                    "created_by": "USLACKBOT",
                    "updated_by": "U060RNRCZ",
                    "deleted_by": null,
                    "prefs": {
                        "channels": [],
                        "groups": []
                    },
                    "user_count": "2"
                },
                {
                    "id": "S06158AV7",
                    "team_id": "T060RNRCH",
                    "is_usergroup": true,
                    "name": "Team Owners",
                    "description": "A group of all Owners on your team.",
                    "handle": "owners",
                    "is_external": false,
                    "date_create": 1446678371,
                    "date_update": 1446678371,
                    "date_delete": 0,
                    "auto_type": "owner",
                    "created_by": "USLACKBOT",
                    "updated_by": "USLACKBOT",
                    "deleted_by": null,
                    "prefs": {
                        "channels": [],
                        "groups": []
                    },
                    "user_count": "1"
                },
                {
                    "id": "S0615G0KT",
                    "team_id": "T060RNRCH",
                    "is_usergroup": true,
                    "name": "Marketing Team",
                    "description": "Marketing gurus, PR experts and product advocates.",
                    "handle": "marketing-team",
                    "is_external": false,
                    "date_create": 1446746793,
                    "date_update": 1446747767,
                    "date_delete": 1446748865,
                    "auto_type": null,
                    "created_by": "U060RNRCZ",
                    "updated_by": "U060RNRCZ",
                    "deleted_by": null,
                    "prefs": {
                        "channels": [],
                        "groups": []
                    },
                    "user_count": "0"
                }
            ]
        }
        """

        payload = {"token": self._token}

        if include_count is not None:
            payload["include_count"] = include_count

        if include_disabled is not None:
            payload["include_disabled"] = include_disabled

        if include_users is not None:
            payload["include_users"] = include_users

        return self._get("usergroups.list", payload=payload, **kwargs)

    def update(
        self,
        usergroup: str,
        channels: str = None,
        description: str = None,
        handle: str = None,
        include_count: bool = None,
        name: str = None,
        **kwargs
    ) -> Response:
        """
        Update an existing User Group
        https://api.slack.com/methods/usergroups.update

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param usergroup: The encoded ID of the User Group to update.
        :type str: e.g. S0604QSJC

        :param channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
        :type str: e.g. C1234567890,C2345678901,C3456789012

        :param description: A short description of the User Group.
        :type str:

        :param handle: A mention handle. Must be unique among channels, users and User Groups.
        :type str: e.g. marketing

        :param include_count: Include the number of users in the User Group.
        :type bool: e.g. true

        :param name: A name for the User Group. Must be unique among User Groups.
        :type str: e.g. My Test Team

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.usergroups.update(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "usergroup": {
                "id": "S0616NG6M",
                "team_id": "T060R4BHN",
                "is_usergroup": true,
                "name": "Marketing Team",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1447096577,
                "date_update": 1447102109,
                "date_delete": 0,
                "auto_type": null,
                "created_by": "U060R4BJ4",
                "updated_by": "U060R4BJ4",
                "deleted_by": null,
                "prefs": {
                    "channels": [],
                    "groups": []
                },
                "users": [
                    "U060R4BJ4",
                    "U060RNRCZ"
                ],
                "user_count": 1
            }
        }
        """

        payload = {"token": self._token, "usergroup": usergroup}

        if channels is not None:
            payload["channels"] = channels

        if description is not None:
            payload["description"] = description

        if handle is not None:
            payload["handle"] = handle

        if include_count is not None:
            payload["include_count"] = include_count

        if name is not None:
            payload["name"] = name

        return self._post("usergroups.update", payload=payload, **kwargs)
