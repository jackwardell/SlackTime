# -*- coding: utf-8 -*-
from requests import Response
from slack_time.api import SlackAPI
from slack_time.utils import cached_property


class Profile(SlackAPI):
    def get(self, visibility: str = None, **kwargs) -> Response:
        """
        Retrieve a team's profile.
        https://api.slack.com/methods/team.profile.get

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param visibility: Filter by visibility.
        :type str: e.g. all

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.team.profile.get(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "profile": {
                "fields": [
                    {
                        "id": "Xf06054AAA",
                        "ordering": 0,
                        "label": "Phone extension",
                        "hint": "Enter the extension to reach your desk",
                        "type": "text",
                        "possible_values": null,
                        "options": null,
                        "is_hidden": 1
                    },
                    {
                        "id": "Xf06054BBB",
                        "ordering": 1,
                        "label": "Date of birth",
                        "hint": "When you were born",
                        "type": "date",
                        "possible_values": null,
                        "options": null
                    },
                    {
                        "id": "Xf06054CCC",
                        "ordering": 2,
                        "label": "Facebook",
                        "hint": "Enter a link to your Facebook profile",
                        "type": "link",
                        "possible_values": null,
                        "options": null
                    },
                    {
                        "id": "Xf06054DDD",
                        "ordering": 3,
                        "label": "House",
                        "hint": "Hogwarts, obviously",
                        "type": "options_list",
                        "possible_values": [
                            "Gryffindor",
                            "Hufflepuff",
                            "Ravenclaw",
                            "Slytherin"
                        ],
                        "options": null
                    },
                    {
                        "id": "Xf06054EEE",
                        "ordering": 4,
                        "label": "Location",
                        "hint": "Office location (LDAP)",
                        "type": "text",
                        "possible_values": null,
                        "options": {
                            "is_protected": 1
                        }
                    },
                    {
                        "id": "Xf06054FFF",
                        "ordering": 5,
                        "label": "Manager",
                        "hint": "The boss",
                        "type": "user",
                        "possible_values": null,
                        "options": null
                    }
                ]
            }
        }
        """

        payload = {"token": self._token}

        if visibility is not None:
            payload["visibility"] = visibility

        return self._get("team.profile.get", payload=payload, **kwargs)


class Team(SlackAPI):
    @cached_property
    def profile(self) -> Profile:
        return Profile(**self.params)

    def access_logs(
        self, before: int = None, count: int = None, page: int = None, **kwargs
    ) -> Response:
        """
        Gets the access logs for the current team.
        https://api.slack.com/methods/team.accessLogs

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param before: End of time range of logs to include in results (inclusive).
        :type int: e.g. 1457989166

        :param count: Number of items to return per page.
        :type int: e.g. 20

        :param page: Page number of results to return.
        :type int: e.g. 2

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.team.access_logs(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "logins": [
                {
                    "user_id": "U45678",
                    "username": "alice",
                    "date_first": 1422922864,
                    "date_last": 1422922864,
                    "count": 1,
                    "ip": "127.0.0.1",
                    "user_agent": "SlackWeb Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.35 Safari/537.36",
                    "isp": "BigCo ISP",
                    "country": "US",
                    "region": "CA"
                },
                {
                    "user_id": "U12345",
                    "username": "white_rabbit",
                    "date_first": 1422922493,
                    "date_last": 1422922493,
                    "count": 1,
                    "ip": "127.0.0.1",
                    "user_agent": "SlackWeb Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",
                    "isp": "BigCo ISP",
                    "country": "US",
                    "region": "CA"
                }
            ],
            "paging": {
                "count": 100,
                "total": 2,
                "page": 1,
                "pages": 1
            }
        }
        """

        payload = {"token": self._token}

        if before is not None:
            payload["before"] = before

        if count is not None:
            payload["count"] = count

        if page is not None:
            payload["page"] = page

        return self._get("team.accessLogs", payload=payload, **kwargs)

    def billable_info(self, user: str = None, **kwargs) -> Response:
        """
        Gets billable users information for the current team.
        https://api.slack.com/methods/team.billableInfo

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param user: A user to retrieve the billable information for. Defaults to all users.
        :type str: e.g. W1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.team.billable_info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "billable_info": {
                "U0632EWRW": {
                    "billing_active": false
                },
                "U02UCPE1R": {
                    "billing_active": true
                },
                "U02UEBSD2": {
                    "billing_active": true
                }
            }
        }
        """

        payload = {"token": self._token}

        if user is not None:
            payload["user"] = user

        return self._get("team.billableInfo", payload=payload, **kwargs)

    def info(self, team: str = None, **kwargs) -> Response:
        """
        Gets information about the current team.
        https://api.slack.com/methods/team.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team: Team to get info on, if omitted, will return information about the current team. Will only return team that the authenticated token is allowed to see through external shared channels
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.team.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "team": {
                "id": "T12345",
                "name": "My Team",
                "domain": "example",
                "email_domain": "example.com",
                "icon": {
                    "image_34": "https://...",
                    "image_44": "https://...",
                    "image_68": "https://...",
                    "image_88": "https://...",
                    "image_102": "https://...",
                    "image_132": "https://...",
                    "image_default": true
                },
                "enterprise_id": "E1234A12AB",
                "enterprise_name": "Umbrella Corporation"
            }
        }
        """

        payload = {"token": self._token}

        if team is not None:
            payload["team"] = team

        return self._get("team.info", payload=payload, **kwargs)

    def integration_logs(
        self,
        app_id: str = None,
        change_type: str = None,
        count: int = None,
        page: int = None,
        service_id: str = None,
        user: str = None,
        **kwargs
    ) -> Response:
        """
        Gets the integration logs for the current team.
        https://api.slack.com/methods/team.integrationLogs

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param app_id: Filter logs to this Slack app. Defaults to all logs.
        :type str:

        :param change_type: Filter logs with this change type. Defaults to all logs.
        :type str: e.g. added

        :param count: Number of items to return per page.
        :type int: e.g. 20

        :param page: Page number of results to return.
        :type int: e.g. 2

        :param service_id: Filter logs to this service. Defaults to all logs.
        :type str:

        :param user: Filter logs generated by this user’s actions. Defaults to all logs.
        :type str: e.g. W1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.team.integration_logs(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if app_id is not None:
            payload["app_id"] = app_id

        if change_type is not None:
            payload["change_type"] = change_type

        if count is not None:
            payload["count"] = count

        if page is not None:
            payload["page"] = page

        if service_id is not None:
            payload["service_id"] = service_id

        if user is not None:
            payload["user"] = user

        return self._get("team.integrationLogs", payload=payload, **kwargs)
