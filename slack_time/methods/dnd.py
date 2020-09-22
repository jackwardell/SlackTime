# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Dnd(SlackAPI):
    def end_dnd(self, **kwargs) -> Response:
        """
        Ends the current user's Do Not Disturb session immediately.
        https://api.slack.com/methods/dnd.endDnd

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.dnd.end_dnd(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        return self._post("dnd.endDnd", payload=payload, **kwargs)

    def end_snooze(self, **kwargs) -> Response:
        """
        Ends the current user's snooze mode immediately.
        https://api.slack.com/methods/dnd.endSnooze

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.dnd.end_snooze(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        return self._post("dnd.endSnooze", payload=payload, **kwargs)

    def info(self, user: str = None, **kwargs) -> Response:
        """
        Retrieves a user's current Do Not Disturb status.
        https://api.slack.com/methods/dnd.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param user: User to fetch status for (defaults to current user)
        :type str: e.g. U1234

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.dnd.info(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if user is not None:
            payload["user"] = user

        return self._get("dnd.info", payload=payload, **kwargs)

    def set_snooze(self, num_minutes: int, **kwargs) -> Response:
        """
        Turns on Do Not Disturb mode for the current user, or changes its duration.
        https://api.slack.com/methods/dnd.setSnooze

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param num_minutes: Number of minutes, from now, to snooze until.
        :type int: e.g. 60

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.dnd.set_snooze(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "num_minutes": num_minutes}

        return self._get("dnd.setSnooze", payload=payload, **kwargs)

    def team_info(self, users: str, **kwargs) -> Response:
        """
        Retrieves the Do Not Disturb status for up to 50 users on a team.
        https://api.slack.com/methods/dnd.teamInfo

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param users: Comma-separated list of users to fetch Do Not Disturb status for
        :type str: e.g. U1234,W4567

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.dnd.team_info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "users": {
                "U023BECGF": {
                    "dnd_enabled": true,
                    "next_dnd_start_ts": 1450387800,
                    "next_dnd_end_ts": 1450423800
                },
                "W058CJVAA": {
                    "dnd_enabled": false,
                    "next_dnd_start_ts": 1,
                    "next_dnd_end_ts": 1
                }
            }
        }
        """

        payload = {"token": self._token, "users": users}

        return self._get("dnd.teamInfo", payload=payload, **kwargs)
