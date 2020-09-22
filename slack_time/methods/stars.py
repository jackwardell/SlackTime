# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Stars(SlackAPI):
    def add(
        self,
        channel: str = None,
        file: str = None,
        file_comment: str = None,
        timestamp: float = None,
        **kwargs
    ) -> Response:
        """
        Adds a star to an item.
        https://api.slack.com/methods/stars.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel to add star to, or channel where the message to add star to was posted (used with timestamp).
        :type str: e.g. C1234567890

        :param file: File to add star to.
        :type str: e.g. F1234567890

        :param file_comment: File comment to add star to.
        :type str: e.g. Fc1234567890

        :param timestamp: Timestamp of the message to add star to.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.stars.add(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if channel is not None:
            payload["channel"] = channel

        if file is not None:
            payload["file"] = file

        if file_comment is not None:
            payload["file_comment"] = file_comment

        if timestamp is not None:
            payload["timestamp"] = timestamp

        return self._post("stars.add", payload=payload, **kwargs)

    def list(
        self,
        count: int = None,
        cursor: str = None,
        limit: int = None,
        page: int = None,
        **kwargs
    ) -> Response:
        """
        Lists stars for a user.
        https://api.slack.com/methods/stars.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param count: Number of items to return per page.
        :type int: e.g. 20

        :param cursor: Parameter for pagination. Set cursor equal to the next_cursor attribute returned by the previous request's response_metadata. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection. See pagination for more details.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
        :type int: e.g. 20

        :param page: Page number of results to return.
        :type int: e.g. 2

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.stars.list(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if count is not None:
            payload["count"] = count

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if page is not None:
            payload["page"] = page

        return self._get("stars.list", payload=payload, **kwargs)

    def remove(
        self,
        channel: str = None,
        file: str = None,
        file_comment: str = None,
        timestamp: float = None,
        **kwargs
    ) -> Response:
        """
        Removes a star from an item.
        https://api.slack.com/methods/stars.remove

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel to remove star from, or channel where the message to remove star from was posted (used with timestamp).
        :type str: e.g. C1234567890

        :param file: File to remove star from.
        :type str: e.g. F1234567890

        :param file_comment: File comment to remove star from.
        :type str: e.g. Fc1234567890

        :param timestamp: Timestamp of the message to remove star from.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.stars.remove(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if channel is not None:
            payload["channel"] = channel

        if file is not None:
            payload["file"] = file

        if file_comment is not None:
            payload["file_comment"] = file_comment

        if timestamp is not None:
            payload["timestamp"] = timestamp

        return self._post("stars.remove", payload=payload, **kwargs)
