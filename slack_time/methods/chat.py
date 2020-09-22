# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property


class ScheduledMessages(SlackAPI):
    def list(
        self,
        channel: str = None,
        cursor: str = None,
        latest: int = None,
        limit: int = None,
        oldest: int = None,
        **kwargs
    ) -> Response:
        """
        Returns a list of scheduled messages.
        https://api.slack.com/methods/chat.scheduledMessages.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: The channel of the scheduled messages
        :type str: e.g. C123456789

        :param cursor: For pagination purposes, this is the cursor value returned from a previous call to chat.scheduledmessages.list indicating where you want to start this call from.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param latest: A UNIX timestamp of the latest value in the time range
        :type int: e.g. 1562137200

        :param limit: Maximum number of original entries to return.
        :type int: e.g. 100

        :param oldest: A UNIX timestamp of the oldest value in the time range
        :type int: e.g. 1562137200

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.scheduled_messages.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "scheduled_messages": [
                {
                    "id": 1298393284,
                    "channel_id": "C1H9RESGL",
                    "post_at": 1551991428,
                    "date_created": 1551891734,
                    "text": "Here's a message for you in the future"
                }
            ],
            "response_metadata": {
                "next_cursor": ""
            }
        }
        """

        payload = {"token": self._token}

        if channel is not None:
            payload["channel"] = channel

        if cursor is not None:
            payload["cursor"] = cursor

        if latest is not None:
            payload["latest"] = latest

        if limit is not None:
            payload["limit"] = limit

        if oldest is not None:
            payload["oldest"] = oldest

        return self._post("chat.scheduledMessages.list", payload=payload, **kwargs)


class Chat(SlackAPI):
    @cached_property
    def scheduled_messages(self) -> ScheduledMessages:
        return ScheduledMessages(**self.params)

    def delete(
        self, channel: str, ts: float, as_user: bool = None, **kwargs
    ) -> Response:
        """
        Deletes a message.
        https://api.slack.com/methods/chat.delete

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel containing the message to be deleted.
        :type str: e.g. C1234567890

        :param ts: Timestamp of the message to be deleted.
        :type float: e.g. 1405894322.002768

        :param as_user: Pass true to delete the message as the authed user with chat:write:user scope. Bot users in this context are considered authed users. If unused or false, the message will be deleted with chat:write:bot scope.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.delete(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": "C024BE91L",
            "ts": "1401383885.000061"
        }
        """

        payload = {"token": self._token, "channel": channel, "ts": ts}

        if as_user is not None:
            payload["as_user"] = as_user

        return self._post("chat.delete", payload=payload, **kwargs)

    def delete_scheduled_message(
        self, channel: str, scheduled_message_id: str, as_user: bool = None, **kwargs
    ) -> Response:
        """
        Deletes a pending scheduled message from the queue.
        https://api.slack.com/methods/chat.deleteScheduledMessage

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: The channel the scheduled_message is posting to
        :type str: e.g. C123456789

        :param scheduled_message_id: scheduled_message_id returned from call to chat.scheduleMessage
        :type str: e.g. Q1234ABCD

        :param as_user: Pass true to delete the message as the authed user with chat:write:user scope. Bot users in this context are considered authed users. If unused or false, the message will be deleted with chat:write:bot scope.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.delete_scheduled_message(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "channel": channel,
            "scheduled_message_id": scheduled_message_id,
        }

        if as_user is not None:
            payload["as_user"] = as_user

        return self._post("chat.deleteScheduledMessage", payload=payload, **kwargs)

    def get_permalink(self, channel: int, message_ts: float, **kwargs) -> Response:
        """
        Retrieve a permalink URL for a specific extant message
        https://api.slack.com/methods/chat.getPermalink

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: The ID of the conversation or channel containing the message
        :type int: e.g. 53072

        :param message_ts: A message's ts value, uniquely identifying it within a channel
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.get_permalink(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": "C1H9RESGA",
            "permalink": "https://ghostbusters.slack.com/archives/C1H9RESGA/p135854651500008"
        }
        """

        payload = {"token": self._token, "channel": channel, "message_ts": message_ts}

        return self._get("chat.getPermalink", payload=payload, **kwargs)

    def me_message(self, channel: str, text: str, **kwargs) -> Response:
        """
        Share a me message into a channel.
        https://api.slack.com/methods/chat.meMessage

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name.
        :type str: e.g. C1234567890

        :param text: Text of the message to send.
        :type str: e.g. Hello world

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.me_message(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": "C024BE7LR",
            "ts": "1417671948.000006"
        }
        """

        payload = {"token": self._token, "channel": channel, "text": text}

        return self._post("chat.meMessage", payload=payload, **kwargs)

    def post_ephemeral(
        self,
        attachments: list,
        channel: str,
        text: str,
        user: str,
        as_user: bool = None,
        blocks: list = None,
        icon_emoji: str = None,
        icon_url: str = None,
        link_names: bool = None,
        parse: str = None,
        thread_ts: float = None,
        username: str = None,
        **kwargs
    ) -> Response:
        """
        Sends an ephemeral message to a user in a channel.
        https://api.slack.com/methods/chat.postEphemeral

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
        :type list: e.g. [{"pretext": "pre-hello", "text": "text-world"}]

        :param channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
        :type str: e.g. C1234567890

        :param text: How this field works and whether it is required depends on other fields you use in your API call. See below for more detail.
        :type str: e.g. Hello world

        :param user: id of the user who will receive the ephemeral message. The user should be in the channel specified by the channel argument.
        :type str: e.g. U0BPQUNTA

        :param as_user: Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false.
        :type bool: e.g. true

        :param blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
        :type list: e.g. [{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]

        :param icon_emoji: Emoji to use as the icon for this message. Overrides icon_url. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below.
        :type str: e.g. :chart_with_upwards_trend:

        :param icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below.
        :type str: e.g. http://lorempixel.com/48/48

        :param link_names: Find and link channel names and usernames.
        :type bool: e.g. true

        :param parse: Change how messages are treated. Defaults to none. See below.
        :type str: e.g. full

        :param thread_ts: Provide another message's ts value to post this message in a thread. Avoid using a reply's ts value; use its parent's value instead. Ephemeral messages in threads are only shown if there is already an active thread.
        :type float: e.g. 1234567890.123456

        :param username: Set your bot's user name. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below.
        :type str: e.g. My Bot

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.post_ephemeral(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "message_ts": "1502210682.580145"
        }
        """

        payload = {
            "token": self._token,
            "attachments": attachments,
            "channel": channel,
            "text": text,
            "user": user,
        }

        if as_user is not None:
            payload["as_user"] = as_user

        if blocks is not None:
            payload["blocks"] = blocks

        if icon_emoji is not None:
            payload["icon_emoji"] = icon_emoji

        if icon_url is not None:
            payload["icon_url"] = icon_url

        if link_names is not None:
            payload["link_names"] = link_names

        if parse is not None:
            payload["parse"] = parse

        if thread_ts is not None:
            payload["thread_ts"] = thread_ts

        if username is not None:
            payload["username"] = username

        return self._post("chat.postEphemeral", payload=payload, **kwargs)

    def post_message(
        self,
        channel: str,
        text: str,
        as_user: bool = None,
        attachments: list = None,
        blocks: list = None,
        icon_emoji: str = None,
        icon_url: str = None,
        link_names: bool = None,
        mrkdwn: bool = None,
        parse: str = None,
        reply_broadcast: bool = None,
        thread_ts: float = None,
        unfurl_links: bool = None,
        unfurl_media: bool = None,
        username: str = None,
        **kwargs
    ) -> Response:
        """
        Sends a message to a channel.
        https://api.slack.com/methods/chat.postMessage

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See below for more details.
        :type str: e.g. C1234567890

        :param text: How this field works and whether it is required depends on other fields you use in your API call. See below for more detail.
        :type str: e.g. Hello world

        :param as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See authorship below. This argument may not be used with newer bot tokens.
        :type bool: e.g. true

        :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
        :type list: e.g. [{"pretext": "pre-hello", "text": "text-world"}]

        :param blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
        :type list: e.g. [{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]

        :param icon_emoji: Emoji to use as the icon for this message. Overrides icon_url. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below. This argument may not be used with newer bot tokens.
        :type str: e.g. :chart_with_upwards_trend:

        :param icon_url: URL to an image to use as the icon for this message. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below. This argument may not be used with newer bot tokens.
        :type str: e.g. http://lorempixel.com/48/48

        :param link_names: Find and link channel names and usernames.
        :type bool: e.g. true

        :param mrkdwn: Disable Slack markup parsing by setting to false. Enabled by default.
        :type bool: e.g. false

        :param parse: Change how messages are treated. Defaults to none. See below.
        :type str: e.g. full

        :param reply_broadcast: Used in conjunction with thread_ts and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to false.
        :type bool: e.g. true

        :param thread_ts: Provide another message's ts value to make this message a reply. Avoid using a reply's ts value; use its parent instead.
        :type float: e.g. 1234567890.123456

        :param unfurl_links: Pass true to enable unfurling of primarily text-based content.
        :type bool: e.g. true

        :param unfurl_media: Pass false to disable unfurling of media content.
        :type bool: e.g. false

        :param username: Set your bot's user name. Must be used in conjunction with as_user set to false, otherwise ignored. See authorship below.
        :type str: e.g. My Bot

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.post_message(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": "C1H9RESGL",
            "ts": "1503435956.000247",
            "message": {
                "text": "Here's a message for you",
                "username": "ecto1",
                "bot_id": "B19LU7CSY",
                "attachments": [
                    {
                        "text": "This is an attachment",
                        "id": 1,
                        "fallback": "This is an attachment's fallback"
                    }
                ],
                "type": "message",
                "subtype": "bot_message",
                "ts": "1503435956.000247"
            }
        }
        """

        payload = {"token": self._token, "channel": channel, "text": text}

        if as_user is not None:
            payload["as_user"] = as_user

        if attachments is not None:
            payload["attachments"] = attachments

        if blocks is not None:
            payload["blocks"] = blocks

        if icon_emoji is not None:
            payload["icon_emoji"] = icon_emoji

        if icon_url is not None:
            payload["icon_url"] = icon_url

        if link_names is not None:
            payload["link_names"] = link_names

        if mrkdwn is not None:
            payload["mrkdwn"] = mrkdwn

        if parse is not None:
            payload["parse"] = parse

        if reply_broadcast is not None:
            payload["reply_broadcast"] = reply_broadcast

        if thread_ts is not None:
            payload["thread_ts"] = thread_ts

        if unfurl_links is not None:
            payload["unfurl_links"] = unfurl_links

        if unfurl_media is not None:
            payload["unfurl_media"] = unfurl_media

        if username is not None:
            payload["username"] = username

        return self._post("chat.postMessage", payload=payload, **kwargs)

    def schedule_message(
        self,
        channel: str,
        post_at: int,
        text: str,
        as_user: bool = None,
        attachments: list = None,
        blocks: list = None,
        link_names: bool = None,
        parse: str = None,
        reply_broadcast: bool = None,
        thread_ts: float = None,
        unfurl_links: bool = None,
        unfurl_media: bool = None,
        **kwargs
    ) -> Response:
        """
        Schedules a message to be sent to a channel.
        https://api.slack.com/methods/chat.scheduleMessage

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See below for more details.
        :type str: e.g. C1234567890

        :param post_at: Unix EPOCH timestamp of time in future to send the message.
        :type int: e.g. 299876400

        :param text: How this field works and whether it is required depends on other fields you use in your API call. See below for more detail.
        :type str: e.g. Hello world

        :param as_user: Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See chat.postMessage.
        :type bool: e.g. true

        :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string.
        :type list: e.g. [{"pretext": "pre-hello", "text": "text-world"}]

        :param blocks: A JSON-based array of structured blocks, presented as a URL-encoded string.
        :type list: e.g. [{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]

        :param link_names: Find and link channel names and usernames.
        :type bool: e.g. true

        :param parse: Change how messages are treated. Defaults to none. See chat.postMessage.
        :type str: e.g. full

        :param reply_broadcast: Used in conjunction with thread_ts and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to false.
        :type bool: e.g. true

        :param thread_ts: Provide another message's ts value to make this message a reply. Avoid using a reply's ts value; use its parent instead.
        :type float: e.g. 1234567890.123456

        :param unfurl_links: Pass true to enable unfurling of primarily text-based content.
        :type bool: e.g. true

        :param unfurl_media: Pass false to disable unfurling of media content.
        :type bool: e.g. false

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.schedule_message(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": "C1H9RESGL",
            "scheduled_message_id": "Q1298393284",
            "post_at": "1562180400",
            "message": {
                "text": "Here's a message for you in the future",
                "username": "ecto1",
                "bot_id": "B19LU7CSY",
                "attachments": [
                    {
                        "text": "This is an attachment",
                        "id": 1,
                        "fallback": "This is an attachment's fallback"
                    }
                ],
                "type": "delayed_message",
                "subtype": "bot_message"
            }
        }
        """

        payload = {
            "token": self._token,
            "channel": channel,
            "post_at": post_at,
            "text": text,
        }

        if as_user is not None:
            payload["as_user"] = as_user

        if attachments is not None:
            payload["attachments"] = attachments

        if blocks is not None:
            payload["blocks"] = blocks

        if link_names is not None:
            payload["link_names"] = link_names

        if parse is not None:
            payload["parse"] = parse

        if reply_broadcast is not None:
            payload["reply_broadcast"] = reply_broadcast

        if thread_ts is not None:
            payload["thread_ts"] = thread_ts

        if unfurl_links is not None:
            payload["unfurl_links"] = unfurl_links

        if unfurl_media is not None:
            payload["unfurl_media"] = unfurl_media

        return self._post("chat.scheduleMessage", payload=payload, **kwargs)

    def unfurl(
        self,
        channel: str,
        ts: float,
        unfurls: dict,
        user_auth_message: str = None,
        user_auth_required: bool = None,
        user_auth_url: str = None,
        **kwargs
    ) -> Response:
        """
        Provide custom unfurl behavior for user-posted URLs
        https://api.slack.com/methods/chat.unfurl

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel ID of the message
        :type str: e.g. C1234567890

        :param ts: Timestamp of the message to add unfurl behavior to.
        :type float: e.g. 1405894322.002768

        :param unfurls: URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments.
        :type dict:

        :param user_auth_message: Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior
        :type str:

        :param user_auth_required: Set to true or 1 to indicate the user must install your Slack app to trigger unfurls for this domain
        :type bool: e.g. true

        :param user_auth_url: Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.
        :type str: e.g. https://example.com/onboarding?user_id=xxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.unfurl(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "channel": channel,
            "ts": ts,
            "unfurls": unfurls,
        }

        if user_auth_message is not None:
            payload["user_auth_message"] = user_auth_message

        if user_auth_required is not None:
            payload["user_auth_required"] = user_auth_required

        if user_auth_url is not None:
            payload["user_auth_url"] = user_auth_url

        return self._post("chat.unfurl", payload=payload, **kwargs)

    def update(
        self,
        channel: str,
        ts: float,
        as_user: bool = None,
        attachments: list = None,
        blocks: list = None,
        link_names: bool = None,
        parse: str = None,
        text: str = None,
        **kwargs
    ) -> Response:
        """
        Updates a message.
        https://api.slack.com/methods/chat.update

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel containing the message to be updated.
        :type str: e.g. C1234567890

        :param ts: Timestamp of the message to be updated.
        :type float: e.g. 1405894322.002768

        :param as_user: Pass true to update the message as the authed user. Bot users in this context are considered authed users.
        :type bool: e.g. true

        :param attachments: A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting text. If you don't include this field, the message's previous attachments will be retained. To remove previous attachments, include an empty array for this field.
        :type list: e.g. [{"pretext": "pre-hello", "text": "text-world"}]

        :param blocks: A JSON-based array of structured blocks, presented as a URL-encoded string. If you don't include this field, the message's previous blocks will be retained. To remove previous blocks, include an empty array for this field.
        :type list: e.g. [{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]

        :param link_names: Find and link channel names and usernames. Defaults to none. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, none.
        :type bool: e.g. true

        :param parse: Change how messages are treated. Defaults to client, unlike chat.postMessage. Accepts either none or full. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, client.
        :type str: e.g. none

        :param text: New text for the message, using the default formatting rules. It's not required when presenting blocks or attachments.
        :type str: e.g. Hello world

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.chat.update(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": "C024BE91L",
            "ts": "1401383885.000061",
            "text": "Updated text you carefully authored",
            "message": {
                "text": "Updated text you carefully authored",
                "user": "U34567890"
            }
        }
        """

        payload = {"token": self._token, "channel": channel, "ts": ts}

        if as_user is not None:
            payload["as_user"] = as_user

        if attachments is not None:
            payload["attachments"] = attachments

        if blocks is not None:
            payload["blocks"] = blocks

        if link_names is not None:
            payload["link_names"] = link_names

        if parse is not None:
            payload["parse"] = parse

        if text is not None:
            payload["text"] = text

        return self._post("chat.update", payload=payload, **kwargs)
