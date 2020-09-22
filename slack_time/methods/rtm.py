# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Rtm(SlackAPI):
    def connect(
        self, batch_presence_aware: int = None, presence_sub: bool = None, **kwargs
    ) -> Response:
        """
        Starts a Real Time Messaging session.
        https://api.slack.com/methods/rtm.connect

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param batch_presence_aware: Batch presence deliveries via subscription. Enabling changes the shape of presence_change events. See batch presence.
        :type int: e.g. 1

        :param presence_sub: Only deliver presence events when requested by subscription. See presence subscriptions.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.rtm.connect(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "self": {
                "id": "U4X318ZMZ",
                "name": "robotoverlord"
            },
            "team": {
                "domain": "slackdemo",
                "id": "T2U81E2FP",
                "name": "SlackDemo"
            },
            "url": "wss://..."
        }
        """

        payload = {"token": self._token}

        if batch_presence_aware is not None:
            payload["batch_presence_aware"] = batch_presence_aware

        if presence_sub is not None:
            payload["presence_sub"] = presence_sub

        return self._get("rtm.connect", payload=payload, **kwargs)

    def start(
        self,
        batch_presence_aware: int = None,
        include_locale: bool = None,
        mpim_aware: bool = None,
        no_latest: int = None,
        no_unreads: bool = None,
        presence_sub: bool = None,
        simple_latest: bool = None,
        **kwargs
    ) -> Response:
        """
        Starts a Real Time Messaging session.
        https://api.slack.com/methods/rtm.start

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param batch_presence_aware: Batch presence deliveries via subscription. Enabling changes the shape of presence_change events. See batch presence.
        :type int: e.g. 1

        :param include_locale: Set this to true to receive the locale for users and channels. Defaults to false
        :type bool: e.g. true

        :param mpim_aware: Returns MPIMs to the client in the API response.
        :type bool: e.g. true

        :param no_latest: Exclude latest timestamps for channels, groups, mpims, and ims. Automatically sets no_unreads to 1
        :type int: e.g. 1

        :param no_unreads: Skip unread counts for each channel (improves performance).
        :type bool: e.g. true

        :param presence_sub: Only deliver presence events when requested by subscription. See presence subscriptions.
        :type bool: e.g. true

        :param simple_latest: Return timestamp only for latest message object of each channel (improves performance).
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.rtm.start(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if batch_presence_aware is not None:
            payload["batch_presence_aware"] = batch_presence_aware

        if include_locale is not None:
            payload["include_locale"] = include_locale

        if mpim_aware is not None:
            payload["mpim_aware"] = mpim_aware

        if no_latest is not None:
            payload["no_latest"] = no_latest

        if no_unreads is not None:
            payload["no_unreads"] = no_unreads

        if presence_sub is not None:
            payload["presence_sub"] = presence_sub

        if simple_latest is not None:
            payload["simple_latest"] = simple_latest

        return self._get("rtm.start", payload=payload, **kwargs)
