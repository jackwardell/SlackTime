# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Migration(SlackAPI):
    def exchange(self, users: str, to_old: bool = None, **kwargs) -> Response:
        """
        For Enterprise Grid workspaces, map local user IDs to global user IDs
        https://api.slack.com/methods/migration.exchange

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param users: A comma-separated list of user ids, up to 400 per request
        :type str:

        :param to_old: Specify true to convert W global user IDs to workspace-specific U IDs. Defaults to false.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.migration.exchange(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "team_id": "T1KR7PE1W",
            "enterprise_id": "E1KQTNXE1",
            "user_id_map": {
                "U06UBSUN5": "W06M56XJM",
                "U06UEB62U": "W06PTT6GH",
                "U06UBSVB3": "W06PUUDLY",
                "U06UBSVDX": "W06PUUDMW",
                "W06UAZ65Q": "W06UAZ65Q"
            },
            "invalid_user_ids": [
                "U21ABZZXX"
            ]
        }
        """

        payload = {"token": self._token, "users": users}

        if to_old is not None:
            payload["to_old"] = to_old

        return self._get("migration.exchange", payload=payload, **kwargs)
