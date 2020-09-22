# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Reminders(SlackAPI):
    def add(self, text: str, time: int, user: str = None, **kwargs) -> Response:
        """
        Creates a reminder.
        https://api.slack.com/methods/reminders.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param text: The content of the reminder
        :type str: e.g. eat a banana

        :param time: When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes," or "every Thursday")
        :type int: e.g. 1602288000

        :param user: The user who will receive the reminder. If no user is specified, the reminder will go to user who created it.
        :type str: e.g. U18888888

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reminders.add(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "text": text, "time": time}

        if user is not None:
            payload["user"] = user

        return self._post("reminders.add", payload=payload, **kwargs)

    def complete(self, reminder: str, **kwargs) -> Response:
        """
        Marks a reminder as complete.
        https://api.slack.com/methods/reminders.complete

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param reminder: The ID of the reminder to be marked as complete
        :type str: e.g. Rm12345678

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reminders.complete(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "reminder": reminder}

        return self._post("reminders.complete", payload=payload, **kwargs)

    def delete(self, reminder: str, **kwargs) -> Response:
        """
        Deletes a reminder.
        https://api.slack.com/methods/reminders.delete

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param reminder: The ID of the reminder
        :type str: e.g. Rm12345678

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reminders.delete(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "reminder": reminder}

        return self._post("reminders.delete", payload=payload, **kwargs)

    def info(self, reminder: str, **kwargs) -> Response:
        """
        Gets information about a reminder.
        https://api.slack.com/methods/reminders.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param reminder: The ID of the reminder
        :type str: e.g. Rm23456789

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reminders.info(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "reminder": reminder}

        return self._get("reminders.info", payload=payload, **kwargs)

    def list(self, **kwargs) -> Response:
        """
        Lists all reminders created by or for a given user.
        https://api.slack.com/methods/reminders.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.reminders.list(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        return self._get("reminders.list", payload=payload, **kwargs)
