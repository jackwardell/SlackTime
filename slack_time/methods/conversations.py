# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Conversations(SlackAPI):
    def archive(self, channel: str, **kwargs) -> Response:
        """
        Archives a conversation.
        https://api.slack.com/methods/conversations.archive

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: ID of conversation to archive
        :type str: e.g. C1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.archive(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel}

        return self._post("conversations.archive", payload=payload, **kwargs)

    def close(self, channel: str, **kwargs) -> Response:
        """
        Closes a direct message or multi-person direct message.
        https://api.slack.com/methods/conversations.close

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Conversation to close.
        :type str: e.g. G1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.close(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel}

        return self._post("conversations.close", payload=payload, **kwargs)

    def create(self, name: str, is_private: bool = None, **kwargs) -> Response:
        """
        Initiates a public or private channel-based conversation
        https://api.slack.com/methods/conversations.create

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: Name of the public or private channel to create
        :type str: e.g. mychannel

        :param is_private: Create a private channel instead of a public one
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.create(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": {
                "id": "C0EAQDV4Z",
                "name": "endeavor",
                "is_channel": true,
                "is_group": false,
                "is_im": false,
                "created": 1504554479,
                "creator": "U0123456",
                "is_archived": false,
                "is_general": false,
                "unlinked": 0,
                "name_normalized": "endeavor",
                "is_shared": false,
                "is_ext_shared": false,
                "is_org_shared": false,
                "pending_shared": [],
                "is_pending_ext_shared": false,
                "is_member": true,
                "is_private": false,
                "is_mpim": false,
                "last_read": "0000000000.000000",
                "latest": null,
                "unread_count": 0,
                "unread_count_display": 0,
                "topic": {
                    "value": "",
                    "creator": "",
                    "last_set": 0
                },
                "purpose": {
                    "value": "",
                    "creator": "",
                    "last_set": 0
                },
                "previous_names": [],
                "priority": 0
            }
        }
        """

        payload = {"token": self._token, "name": name}

        if is_private is not None:
            payload["is_private"] = is_private

        return self._post("conversations.create", payload=payload, **kwargs)

    def history(
        self,
        channel: str,
        cursor: str = None,
        inclusive: bool = None,
        latest: float = None,
        limit: int = None,
        oldest: float = None,
        **kwargs
    ) -> Response:
        """
        Fetches a conversation's history of messages and events.
        https://api.slack.com/methods/conversations.history

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Conversation ID to fetch history for.
        :type str: e.g. C1234567890

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is specified.
        :type bool: e.g. true

        :param latest: End of time range of messages to include in results.
        :type float: e.g. 1234567890.123456

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
        :type int: e.g. 20

        :param oldest: Start of time range of messages to include in results.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.history(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "messages": [
                {
                    "type": "message",
                    "user": "U012AB3CDE",
                    "text": "I find you punny and would like to smell your nose letter",
                    "ts": "1512085950.000216"
                },
                {
                    "type": "message",
                    "user": "U061F7AUR",
                    "text": "What, you want to smell my shoes better?",
                    "ts": "1512104434.000490"
                }
            ],
            "has_more": true,
            "pin_count": 0,
            "response_metadata": {
                "next_cursor": "bmV4dF90czoxNTEyMDg1ODYxMDAwNTQz"
            }
        }
        """

        payload = {"token": self._token, "channel": channel}

        if cursor is not None:
            payload["cursor"] = cursor

        if inclusive is not None:
            payload["inclusive"] = inclusive

        if latest is not None:
            payload["latest"] = latest

        if limit is not None:
            payload["limit"] = limit

        if oldest is not None:
            payload["oldest"] = oldest

        return self._get("conversations.history", payload=payload, **kwargs)

    def info(
        self,
        channel: str,
        include_locale: bool = None,
        include_num_members: bool = None,
        **kwargs
    ) -> Response:
        """
        Retrieve information about a conversation.
        https://api.slack.com/methods/conversations.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Conversation ID to learn more about
        :type str: e.g. C1234567890

        :param include_locale: Set this to true to receive the locale for this conversation. Defaults to false
        :type bool: e.g. true

        :param include_num_members: Set to true to include the member count for the specified conversation. Defaults to false
        :type bool: e.g. true


        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": {
                "id": "C012AB3CD",
                "name": "general",
                "is_channel": true,
                "is_group": false,
                "is_im": false,
                "created": 1449252889,
                "creator": "W012A3BCD",
                "is_archived": false,
                "is_general": true,
                "unlinked": 0,
                "name_normalized": "general",
                "is_read_only": false,
                "is_shared": false,
                "parent_conversation": null,
                "is_ext_shared": false,
                "is_org_shared": false,
                "pending_shared": [],
                "is_pending_ext_shared": false,
                "is_member": true,
                "is_private": false,
                "is_mpim": false,
                "last_read": "1502126650.228446",
                "topic": {
                    "value": "For public discussion of generalities",
                    "creator": "W012A3BCD",
                    "last_set": 1449709364
                },
                "purpose": {
                    "value": "This part of the workspace is for fun. Make fun here.",
                    "creator": "W012A3BCD",
                    "last_set": 1449709364
                },
                "previous_names": [
                    "specifics",
                    "abstractions",
                    "etc"
                ],
                "locale": "en-US"
            }
        }
        """

        payload = {"token": self._token, "channel": channel}

        if include_locale is not None:
            payload["include_locale"] = include_locale

        if include_num_members is not None:
            payload["include_num_members"] = include_num_members

        return self._get("conversations.info", payload=payload, **kwargs)

    def invite(self, channel: str, users: str, **kwargs) -> Response:
        """
        Invites users to a channel.
        https://api.slack.com/methods/conversations.invite

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: The ID of the public or private channel to invite user(s) to.
        :type str: e.g. C1234567890

        :param users: A comma separated list of user IDs. Up to 1000 users may be listed.
        :type str: e.g. W1234567890,U2345678901,U3456789012

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.invite(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": {
                "id": "C012AB3CD",
                "name": "general",
                "is_channel": true,
                "is_group": false,
                "is_im": false,
                "created": 1449252889,
                "creator": "W012A3BCD",
                "is_archived": false,
                "is_general": true,
                "unlinked": 0,
                "name_normalized": "general",
                "is_read_only": false,
                "is_shared": false,
                "is_ext_shared": false,
                "is_org_shared": false,
                "pending_shared": [],
                "is_pending_ext_shared": false,
                "is_member": true,
                "is_private": false,
                "is_mpim": false,
                "last_read": "1502126650.228446",
                "topic": {
                    "value": "For public discussion of generalities",
                    "creator": "W012A3BCD",
                    "last_set": 1449709364
                },
                "purpose": {
                    "value": "This part of the workspace is for fun. Make fun here.",
                    "creator": "W012A3BCD",
                    "last_set": 1449709364
                },
                "previous_names": [
                    "specifics",
                    "abstractions",
                    "etc"
                ],
                "num_members": 23,
                "locale": "en-US"
            }
        }
        """

        payload = {"token": self._token, "channel": channel, "users": users}

        return self._post("conversations.invite", payload=payload, **kwargs)

    def join(self, channel: str, **kwargs) -> Response:
        """
        Joins an existing conversation.
        https://api.slack.com/methods/conversations.join

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: ID of conversation to join
        :type str: e.g. C1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.join(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": {
                "id": "C061EG9SL",
                "name": "general",
                "is_channel": true,
                "is_group": false,
                "is_im": false,
                "created": 1449252889,
                "creator": "U061F7AUR",
                "is_archived": false,
                "is_general": true,
                "unlinked": 0,
                "name_normalized": "general",
                "is_shared": false,
                "is_ext_shared": false,
                "is_org_shared": false,
                "pending_shared": [],
                "is_pending_ext_shared": false,
                "is_member": true,
                "is_private": false,
                "is_mpim": false,
                "topic": {
                    "value": "Which widget do you worry about?",
                    "creator": "",
                    "last_set": 0
                },
                "purpose": {
                    "value": "For widget discussion",
                    "creator": "",
                    "last_set": 0
                },
                "previous_names": []
            },
            "warning": "already_in_channel",
            "response_metadata": {
                "warnings": [
                    "already_in_channel"
                ]
            }
        }
        """

        payload = {"token": self._token, "channel": channel}

        return self._post("conversations.join", payload=payload, **kwargs)

    def kick(self, channel: str, user: str, **kwargs) -> Response:
        """
        Removes a user from a conversation.
        https://api.slack.com/methods/conversations.kick

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: ID of conversation to remove user from.
        :type str: e.g. C1234567890

        :param user: User ID to be removed.
        :type str: e.g. W1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.kick(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel, "user": user}

        return self._post("conversations.kick", payload=payload, **kwargs)

    def leave(self, channel: str, **kwargs) -> Response:
        """
        Leaves a conversation.
        https://api.slack.com/methods/conversations.leave

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Conversation to leave
        :type str: e.g. C1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.leave(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel}

        return self._post("conversations.leave", payload=payload, **kwargs)

    def list(
        self,
        cursor: str = None,
        exclude_archived: bool = None,
        limit: int = None,
        types: str = None,
        **kwargs
    ) -> Response:
        """
        Lists all channels in a Slack team.
        https://api.slack.com/methods/conversations.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param exclude_archived: Set to true to exclude archived channels from the list
        :type bool: e.g. true

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.
        :type int: e.g. 20

        :param types: Mix and match channel types by providing a comma-separated list of any combination of public_channel, private_channel, mpim, im
        :type str: e.g. public_channel,private_channel

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channels": [
                {
                    "id": "C012AB3CD",
                    "name": "general",
                    "is_channel": true,
                    "is_group": false,
                    "is_im": false,
                    "created": 1449252889,
                    "creator": "U012A3CDE",
                    "is_archived": false,
                    "is_general": true,
                    "unlinked": 0,
                    "name_normalized": "general",
                    "is_shared": false,
                    "is_ext_shared": false,
                    "is_org_shared": false,
                    "pending_shared": [],
                    "is_pending_ext_shared": false,
                    "is_member": true,
                    "is_private": false,
                    "is_mpim": false,
                    "topic": {
                        "value": "Company-wide announcements and work-based matters",
                        "creator": "",
                        "last_set": 0
                    },
                    "purpose": {
                        "value": "This channel is for team-wide communication and announcements. All team members are in this channel.",
                        "creator": "",
                        "last_set": 0
                    },
                    "previous_names": [],
                    "num_members": 4
                },
                {
                    "id": "C061EG9T2",
                    "name": "random",
                    "is_channel": true,
                    "is_group": false,
                    "is_im": false,
                    "created": 1449252889,
                    "creator": "U061F7AUR",
                    "is_archived": false,
                    "is_general": false,
                    "unlinked": 0,
                    "name_normalized": "random",
                    "is_shared": false,
                    "is_ext_shared": false,
                    "is_org_shared": false,
                    "pending_shared": [],
                    "is_pending_ext_shared": false,
                    "is_member": true,
                    "is_private": false,
                    "is_mpim": false,
                    "topic": {
                        "value": "Non-work banter and water cooler conversation",
                        "creator": "",
                        "last_set": 0
                    },
                    "purpose": {
                        "value": "A place for non-work-related flimflam, faffing, hodge-podge or jibber-jabber you'd prefer to keep out of more focused work-related channels.",
                        "creator": "",
                        "last_set": 0
                    },
                    "previous_names": [],
                    "num_members": 4
                }
            ],
            "response_metadata": {
                "next_cursor": "dGVhbTpDMDYxRkE1UEI="
            }
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if exclude_archived is not None:
            payload["exclude_archived"] = exclude_archived

        if limit is not None:
            payload["limit"] = limit

        if types is not None:
            payload["types"] = types

        return self._get("conversations.list", payload=payload, **kwargs)

    def mark(self, channel: str, ts: float, **kwargs) -> Response:
        """
        Sets the read cursor in a channel.
        https://api.slack.com/methods/conversations.mark

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Channel or conversation to set the read cursor for.
        :type str: e.g. C012345678

        :param ts: Unique identifier of message you want marked as most recently seen in this conversation.
        :type float: e.g. 1593473566.000200

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.mark(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel, "ts": ts}

        return self._post("conversations.mark", payload=payload, **kwargs)

    def members(
        self, channel: str, cursor: str = None, limit: int = None, **kwargs
    ) -> Response:
        """
        Retrieve members of a conversation.
        https://api.slack.com/methods/conversations.members

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: ID of the conversation to retrieve members for
        :type str: e.g. C1234567890

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
        :type int: e.g. 20

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.members(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "members": [
                "U023BECGF",
                "U061F7AUR",
                "W012A3CDE"
            ],
            "response_metadata": {
                "next_cursor": "e3VzZXJfaWQ6IFcxMjM0NTY3fQ=="
            }
        }
        """

        payload = {"token": self._token, "channel": channel}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._get("conversations.members", payload=payload, **kwargs)

    def open(
        self, channel: str = None, return_im: bool = None, users: str = None, **kwargs
    ) -> Response:
        """
        Opens or resumes a direct message or multi-person direct message.
        https://api.slack.com/methods/conversations.open

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Resume a conversation by supplying an im or mpim's ID. Or provide the users field instead.
        :type str: e.g. G1234567890

        :param return_im: Boolean, indicates you want the full IM channel definition in the response.
        :type bool: e.g. true

        :param users: Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a channel when not supplying users.
        :type str: e.g. W1234567890,U2345678901,U3456789012

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.open(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": {
                "id": "D069C7QFK"
            }
        }
        """

        payload = {"token": self._token}

        if channel is not None:
            payload["channel"] = channel

        if return_im is not None:
            payload["return_im"] = return_im

        if users is not None:
            payload["users"] = users

        return self._post("conversations.open", payload=payload, **kwargs)

    def rename(self, channel: str, name: str, **kwargs) -> Response:
        """
        Renames a conversation.
        https://api.slack.com/methods/conversations.rename

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: ID of conversation to rename
        :type str: e.g. C1234567890

        :param name: New name for conversation.
        :type str: new-convo

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.rename(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel": {
                "id": "C012AB3CD",
                "name": "general",
                "is_channel": true,
                "is_group": false,
                "is_im": false,
                "created": 1449252889,
                "creator": "W012A3BCD",
                "is_archived": false,
                "is_general": true,
                "unlinked": 0,
                "name_normalized": "general",
                "is_read_only": false,
                "is_shared": false,
                "is_ext_shared": false,
                "is_org_shared": false,
                "pending_shared": [],
                "is_pending_ext_shared": false,
                "is_member": true,
                "is_private": false,
                "is_mpim": false,
                "last_read": "1502126650.228446",
                "topic": {
                    "value": "For public discussion of generalities",
                    "creator": "W012A3BCD",
                    "last_set": 1449709364
                },
                "purpose": {
                    "value": "This part of the workspace is for fun. Make fun here.",
                    "creator": "W012A3BCD",
                    "last_set": 1449709364
                },
                "previous_names": [
                    "specifics",
                    "abstractions",
                    "etc"
                ],
                "num_members": 23,
                "locale": "en-US"
            }
        }
        """

        payload = {"token": self._token, "channel": channel, "name": name}

        return self._post("conversations.rename", payload=payload, **kwargs)

    def replies(
        self,
        channel: str,
        ts: float,
        cursor: str = None,
        inclusive: bool = None,
        latest: float = None,
        limit: int = None,
        oldest: float = None,
        **kwargs
    ) -> Response:
        """
        Retrieve a thread of messages posted to a conversation
        https://api.slack.com/methods/conversations.replies

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Conversation ID to fetch thread from.
        :type str: e.g. C1234567890

        :param ts: Unique identifier of a thread's parent message. ts must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by ts will return - it is just an ordinary, unthreaded message.
        :type float: e.g. 1234567890.123456

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param inclusive: Include messages with latest or oldest timestamp in results only when either timestamp is specified.
        :type bool: e.g. true

        :param latest: End of time range of messages to include in results.
        :type float: e.g. 1234567890.123456

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
        :type int: e.g. 20

        :param oldest: Start of time range of messages to include in results.
        :type float: e.g. 1234567890.123456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.replies(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "messages": [
                {
                    "type": "message",
                    "user": "U061F7AUR",
                    "text": "island",
                    "thread_ts": "1482960137.003543",
                    "reply_count": 3,
                    "subscribed": true,
                    "last_read": "1484678597.521003",
                    "unread_count": 0,
                    "ts": "1482960137.003543"
                },
                {
                    "type": "message",
                    "user": "U061F7AUR",
                    "text": "one island",
                    "thread_ts": "1482960137.003543",
                    "parent_user_id": "U061F7AUR",
                    "ts": "1483037603.017503"
                },
                {
                    "type": "message",
                    "user": "U061F7AUR",
                    "text": "two island",
                    "thread_ts": "1482960137.003543",
                    "parent_user_id": "U061F7AUR",
                    "ts": "1483051909.018632"
                },
                {
                    "type": "message",
                    "user": "U061F7AUR",
                    "text": "three for the land",
                    "thread_ts": "1482960137.003543",
                    "parent_user_id": "U061F7AUR",
                    "ts": "1483125339.020269"
                }
            ],
            "has_more": true,
            "ok": true,
            "response_metadata": {
                "next_cursor": "bmV4dF90czoxNDg0Njc4MjkwNTE3MDkx"
            }
        }
        """

        payload = {"token": self._token, "channel": channel, "ts": ts}

        if cursor is not None:
            payload["cursor"] = cursor

        if inclusive is not None:
            payload["inclusive"] = inclusive

        if latest is not None:
            payload["latest"] = latest

        if limit is not None:
            payload["limit"] = limit

        if oldest is not None:
            payload["oldest"] = oldest

        return self._get("conversations.replies", payload=payload, **kwargs)

    def set_purpose(self, channel: str, purpose: str, **kwargs) -> Response:
        """
        Sets the purpose for a conversation.
        https://api.slack.com/methods/conversations.setPurpose

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Conversation to set the purpose of
        :type str: e.g. C1234567890

        :param purpose: A new, specialer purpose
        :type str: e.g. My More Special Purpose

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.set_purpose(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "purpose": "I didn't set this purpose on purpose!"
        }

        """

        payload = {"token": self._token, "channel": channel, "purpose": purpose}

        return self._post("conversations.setPurpose", payload=payload, **kwargs)

    def set_topic(self, channel: str, topic: str, **kwargs) -> Response:
        """
        Sets the topic for a conversation.
        https://api.slack.com/methods/conversations.setTopic

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Conversation to set the topic of
        :type str: e.g. C1234567890

        :param topic: The new topic string. Does not support formatting or linkification.
        :type str: e.g. Apply topically for best effects

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.set_topic(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "topic": "Apply topically for best effects"
        }

        """

        payload = {"token": self._token, "channel": channel, "topic": topic}

        return self._post("conversations.setTopic", payload=payload, **kwargs)

    def unarchive(self, channel: str, **kwargs) -> Response:
        """
        Reverses conversation archival.
        https://api.slack.com/methods/conversations.unarchive

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: ID of conversation to unarchive
        :type str: e.g. C1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.conversations.unarchive(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel": channel}

        return self._post("conversations.unarchive", payload=payload, **kwargs)
