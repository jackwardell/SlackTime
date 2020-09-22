# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Api(SlackAPI):
    def test(self, error: str = None, foo: str = None, **kwargs) -> Response:
        """
        Checks API calling code.
        https://api.slack.com/methods/api.test

        :param error: Error response to return
        :type str: e.g. my_error

        :param foo: example property to return
        :type str: e.g. bar

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.api.test(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token}

        if error is not None:
            payload["error"] = error

        if foo is not None:
            payload["foo"] = foo

        return self._post("api.test", payload=payload, **kwargs)
