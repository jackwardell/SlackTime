# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Bots(SlackAPI):
    def info(self, bot: str = None, **kwargs) -> Response:
        """
        Gets information about a bot user.
        https://api.slack.com/methods/bots.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param bot: Bot user to get info on
        :type str: e.g. B12345678

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.bots.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "bot": {
                "id": "B061F7JD2",
                "deleted": false,
                "name": "beforebot",
                "updated": 1449272004,
                "app_id": "A161CLERW",
                "user_id": "U012ABCDEF",
                "icons": {
                    "image_36": "https://...",
                    "image_48": "https://...",
                    "image_72": "https://..."
                }
            }
        }
        """

        payload = {"token": self._token}

        if bot is not None:
            payload["bot"] = bot

        return self._get("bots.info", payload=payload, **kwargs)
