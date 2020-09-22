# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Emoji(SlackAPI):
    def list(self, **kwargs) -> Response:
        """
        Lists custom emoji for a team.
        https://api.slack.com/methods/emoji.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.emoji.list(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        return self._get("emoji.list", payload=payload, **kwargs)
