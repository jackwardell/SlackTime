# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property


class Approved(SlackAPI):
    def list(
        self,
        cursor: str = None,
        enterprise_id: str = None,
        limit: int = None,
        team_id: str = None,
        **kwargs
    ) -> Response:
        """
        List approved apps for an org or workspace.
        https://api.slack.com/methods/admin.apps.approved.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page
        :type str: e.g. 5c3e53d5

        :param enterprise_id:
        :type str: e.g. E0AS553RN

        :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
        :type int: e.g. 100

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.apps.approved.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "approved_apps": [
                {
                    "app": {
                        "id": "A0W7UKG8E",
                        "name": "My Test App",
                        "description": "test app",
                        "help_url": "https://www.slack.com",
                        "privacy_policy_url": "https://www.slack.com",
                        "app_homepage_url": "https://www.slack.com",
                        "app_directory_url": "https://myteam.enterprise.slack.com/apps/A0W7UKG8E-my-test-app",
                        "is_app_directory_approved": false,
                        "is_internal": false,
                        "icons": {
                            "image_32": "https://302674312496446w_2bd4ea1ad1f89a23c242_32.png",
                            "image_36": "https://302674312496446w_2bd4ea1ad1f89a23c242_36.png",
                            "image_48": "https://302674312496446w_2bd4ea1ad1f89a23c242_48.png",
                            "image_64": "https://302674312496446w_2bd4ea1ad1f89a23c242_64.png",
                            "image_72": "https://302674312496446w_2bd4ea1ad1f89a23c242_72.png",
                            "image_96": "https://302674312496446w_2bd4ea1ad1f89a23c242_96.png",
                            "image_128": "https://30267341249446w6_2bd4ea1ad1f89a23c242_128.png",
                            "image_192": "https://30267431249446w6_2bd4ea1ad1f89a23c242_192.png",
                            "image_512": "https://30267431249446w6_2bd4ea1ad1f89a23c242_512.png",
                            "image_1024": "https://3026743124446w96_2bd4ea1ad1f89a23c242_1024.png",
                            "image_original": "https://302674446w12496_2bd4ea1ad1f89a23c242_original.png"
                        },
                        "additional_info": ""
                    },
                    "scopes": [
                        {
                            "name": "bot",
                            "description": "Add the ability for people to direct message or mention @my_test_app",
                            "is_sensitive": true,
                            "token_type": "bot"
                        }
                    ],
                    "date_updated": 1574296707,
                    "last_resolved_by": {
                        "actor_id": "W0G82F4FD",
                        "actor_type": "user"
                    }
                }
            ],
            "response_metadata": {
                "next_cursor": ""
            }
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if enterprise_id is not None:
            payload["enterprise_id"] = enterprise_id

        if limit is not None:
            payload["limit"] = limit

        if team_id is not None:
            payload["team_id"] = team_id

        return self._get("admin.apps.approved.list", payload=payload, **kwargs)


class Requests(SlackAPI):
    def list(
        self, cursor: str = None, limit: int = None, team_id: str = None, **kwargs
    ) -> Response:
        """
        List app requests for a team/workspace.
        https://api.slack.com/methods/admin.apps.requests.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page
        :type str: e.g. 5c3e53d5

        :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
        :type int: e.g. 100

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.apps.requests.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "app_requests": [
                {
                    "id": "Ar0XJGFLMLS",
                    "app": {
                        "id": "A061BL8RQ0",
                        "name": "Test App",
                        "description": "",
                        "help_url": "",
                        "privacy_policy_url": "https://testapp.com/privacy",
                        "app_homepage_url": "",
                        "app_directory_url": "https://acmecorp.slack.com/apps/A061BL8RQ0-test-app",
                        "is_app_directory_approved": true,
                        "is_internal": false,
                        "icons": {
                            "image_32": "/cdn/157658203/img/testapp/service_32.png",
                            "image_36": "/cdn/157658203/img/testapp/service_36.png",
                            "image_48": "/cdn/157658203/img/testapp/service_48.png",
                            "image_64": "/cdn/157658203/img/testapp/service_64.png",
                            "image_72": "/cdn/157658203/img/testapp/service_72.png",
                            "image_96": "/cdn/157658203/img/testapp/service_96.png",
                            "image_128": "/cdn/157258203/img/testapp/service_128.png",
                            "image_192": "/cdn/157258203/img/testapp/service_192.png",
                            "image_512": "/cdn/15758203/img/testapp/service_512.png",
                            "image_1024": "/cdn/15258203/img/testapp/service_1024.png"
                        },
                        "additional_info": ""
                    },
                    "previous_resolution": null,
                    "user": {
                        "id": "W08RA9G5HR",
                        "name": "Jane Doe",
                        "email": "janedoe@example.com"
                    },
                    "team": {
                        "id": "T0M94LNUCR",
                        "name": "Acme Corp",
                        "domain": "acmecorp"
                    },
                    "scopes": [
                        {
                            "name": "incoming-webhook",
                            "description": "Post messages to specific channels in Slack",
                            "is_sensitive": false,
                            "token_type": "user"
                        }
                    ],
                    "message": "test test again",
                    "date_created": 1578956327
                }
            ],
            "response_metadata": {
                "next_cursor": ""
            }
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if team_id is not None:
            payload["team_id"] = team_id

        return self._get("admin.apps.requests.list", payload=payload, **kwargs)


class Restricted(SlackAPI):
    def list(
        self,
        cursor: str = None,
        enterprise_id: str = None,
        limit: int = None,
        team_id: str = None,
        **kwargs
    ) -> Response:
        """
        List restricted apps for an org or workspace.
        https://api.slack.com/methods/admin.apps.restricted.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page
        :type str: e.g. 5c3e53d5

        :param enterprise_id:
        :type str: e.g. E0AS553RN

        :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
        :type int: e.g. 100

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.apps.restricted.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "restricted_apps": [
                {
                    "app": {
                        "id": "A0FDLP8M2L",
                        "name": "My Test App",
                        "description": "A fun test app for Slack",
                        "help_url": "https://example.com",
                        "privacy_policy_url": "https://example.com",
                        "app_homepage_url": "https://example.com",
                        "app_directory_url": "https://myteam.enterprise.slack.com/apps/A0FDLP8M2L-my-test-app",
                        "is_app_directory_approved": true,
                        "is_internal": false,
                        "icons": {
                            "image_32": "https://143326534038rl8788_eb57dbc818daa4ba15d6_32.png",
                            "image_36": "https://143326534038rl8788_eb57dbc818daa4ba15d6_36.png",
                            "image_48": "https://143326534038rl8788_eb57dbc818daa4ba15d6_48.png",
                            "image_64": "https://143326534038rl8788_eb57dbc818daa4ba15d6_64.png",
                            "image_72": "https://143326534038rl8788_eb57dbc818daa4ba15d6_72.png",
                            "image_96": "https://143326534038rl8788_eb57dbc818daa4ba15d6_96.png",
                            "image_128": "https://4332653438rl87808_eb57dbc818daa4ba15d6_128.png",
                            "image_192": "https://4332653438rl87808_eb57dbc818daa4ba15d6_192.png",
                            "image_512": "https://4332653438rl87808_eb57dbc818daa4ba15d6_512.png",
                            "image_1024": "https://1433265338rl878408_eb57dbc818daa4ba15d6_1024.png",
                            "image_original": "https://143338rl8782653408_eb57dbc818daa4ba15d6_original.png"
                        },
                        "additional_info": ""
                    },
                    "scopes": [
                        {
                            "name": "files:write:user",
                            "description": "Upload, edit, and delete files on the user\u201fs behalf",
                            "is_sensitive": true,
                            "token_type": "user"
                        }
                    ],
                    "date_updated": 1574296721,
                    "last_resolved_by": {
                        "actor_id": "W0G82LMFD",
                        "actor_type": "user"
                    }
                }
            ],
            "response_metadata": {
                "next_cursor": ""
            }
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if enterprise_id is not None:
            payload["enterprise_id"] = enterprise_id

        if limit is not None:
            payload["limit"] = limit

        if team_id is not None:
            payload["team_id"] = team_id

        return self._get("admin.apps.restricted.list", payload=payload, **kwargs)


class Apps(SlackAPI):
    def approve(
        self, app_id: str = None, request_id: str = None, team_id: str = None, **kwargs
    ) -> Response:
        """
        Approve an app for installation on a workspace.
        https://api.slack.com/methods/admin.apps.approve

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param app_id: The id of the app to approve.
        :type str: e.g. A12345

        :param request_id: The id of the request to approve.
        :type str: e.g. Ar12345

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.apps.approve(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token}

        if app_id is not None:
            payload["app_id"] = app_id

        if request_id is not None:
            payload["request_id"] = request_id

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.apps.approve", payload=payload, **kwargs)

    def restrict(
        self, app_id: str = None, request_id: str = None, team_id: str = None, **kwargs
    ) -> Response:
        """
        Restrict an app for installation on a workspace.
        https://api.slack.com/methods/admin.apps.restrict

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param app_id: The id of the app to restrict.
        :type str: e.g. A12345

        :param request_id: The id of the request to restrict.
        :type str: e.g. Ar12345

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.apps.restrict(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token}

        if app_id is not None:
            payload["app_id"] = app_id

        if request_id is not None:
            payload["request_id"] = request_id

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.apps.restrict", payload=payload, **kwargs)

    @cached_property
    def approved(self) -> Approved:
        return Approved(**self.params)

    @cached_property
    def requests(self) -> Requests:
        return Requests(**self.params)

    @cached_property
    def restricted(self) -> Restricted:
        return Restricted(**self.params)


class Ekm(SlackAPI):
    def list_original_connected_channel_info(
        self,
        channel_ids: str = None,
        cursor: str = None,
        limit: int = None,
        team_ids: str = None,
        **kwargs
    ) -> Response:
        """
        List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.
        https://api.slack.com/methods/admin.conversations.ekm.listOriginalConnectedChannelInfo

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_ids: A comma-separated list of channels to filter to.
        :type str:
        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page.
        :type str: e.g. 5c3e53d5

        :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
        :type int: e.g. 100

        :param team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.ekm.list_original_connected_channel_info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channels": [
                {
                    "id": "string",
                    "internal_team_ids": "array",
                    "original_connected_host_id": "string",
                    "original_connected_channel_id": "string"
                }
            ]
        }
        """

        payload = {"token": self._token}

        if channel_ids is not None:
            payload["channel_ids"] = channel_ids

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if team_ids is not None:
            payload["team_ids"] = team_ids

        return self._get(
            "admin.conversations.ekm.listOriginalConnectedChannelInfo",
            payload=payload,
            **kwargs
        )


class RestrictAccess(SlackAPI):
    def add_group(
        self, channel_id: str, group_id: str, team_id: str = None, **kwargs
    ) -> Response:
        """
        Add an allowlist of IDP groups for accessing a channel
        https://api.slack.com/methods/admin.conversations.restrictAccess.addGroup

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to link this group to.
        :type str:

        :param group_id: The IDP Group ID to be an allowlist for the private channel.
        :type str:

        :param team_id: The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.restrict_access.add_group(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id, "group_id": group_id}

        if team_id is not None:
            payload["team_id"] = team_id

        return self._get(
            "admin.conversations.restrictAccess.addGroup", payload=payload, **kwargs
        )

    def list_groups(self, channel_id: str, team_id: str = None, **kwargs) -> Response:
        """
        List all IDP Groups linked to a channel
        https://api.slack.com/methods/admin.conversations.restrictAccess.listGroups

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id:
        :type str:

        :param team_id: The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.restrict_access.list_groups(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "group_ids": [
                "YOUR_GROUP_ID"
            ]
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        if team_id is not None:
            payload["team_id"] = team_id

        return self._get(
            "admin.conversations.restrictAccess.listGroups", payload=payload, **kwargs
        )

    def remove_group(
        self, channel_id: str, group_id: str, team_id: str, **kwargs
    ) -> Response:
        """
        Remove a linked IDP group linked from a private channel
        https://api.slack.com/methods/admin.conversations.restrictAccess.removeGroup

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to remove the linked group from.
        :type str:

        :param group_id: The IDP Group ID to remove from the private channel.
        :type str:

        :param team_id: The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.restrict_access.remove_group(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "channel_id": channel_id,
            "group_id": group_id,
            "team_id": team_id,
        }

        return self._get(
            "admin.conversations.restrictAccess.removeGroup", payload=payload, **kwargs
        )


class Conversations(SlackAPI):
    @cached_property
    def ekm(self) -> Ekm:
        return Ekm(**self.params)

    @cached_property
    def restrict_access(self) -> RestrictAccess:
        return RestrictAccess(**self.params)

    def archive(self, channel_id: str, **kwargs) -> Response:
        """
        Archive a public or private channel.
        https://api.slack.com/methods/admin.conversations.archive

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to archive.
        :type str: e.g. C12345

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.archive(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        return self._post("admin.conversations.archive", payload=payload, **kwargs)

    def convert_to_private(self, channel_id: str, **kwargs) -> Response:
        """
        Convert a public channel to a private channel.
        https://api.slack.com/methods/admin.conversations.convertToPrivate

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to convert to private.
        :type str: e.g. C12345

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.convert_to_private(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        return self._post(
            "admin.conversations.convertToPrivate", payload=payload, **kwargs
        )

    def create(
        self,
        is_private: bool,
        name: str,
        description: str = None,
        org_wide: bool = None,
        team_id: str = None,
        **kwargs
    ) -> Response:
        """
        Create a public or private channel-based conversation.
        https://api.slack.com/methods/admin.conversations.create

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param is_private: When true, creates a private channel instead of a public channel
        :type bool: e.g. true

        :param name: Name of the public or private channel to create.
        :type str: e.g. mychannel

        :param description: Description of the public or private channel to create.
        :type str: e.g. It's a good channel, Bront.

        :param org_wide: When true, the channel will be available org-wide. Note: if the channel is not org_wide=true, you must specify a team_id for this channel
        :type bool: e.g. true

        :param team_id: The workspace to create the channel in. Note: this argument is required unless you set org_wide=true.
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.create(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channel_id": "C12345"
        }
        """

        payload = {"token": self._token, "is_private": is_private, "name": name}

        if description is not None:
            payload["description"] = description

        if org_wide is not None:
            payload["org_wide"] = org_wide

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.conversations.create", payload=payload, **kwargs)

    def delete(self, channel_id: str, **kwargs) -> Response:
        """
        Delete a public or private channel.
        https://api.slack.com/methods/admin.conversations.delete

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to delete.
        :type str: e.g. C12345

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.delete(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        return self._post("admin.conversations.delete", payload=payload, **kwargs)

    def disconnect_shared(
        self, channel_id: str, leaving_team_ids: str = None, **kwargs
    ) -> Response:
        """
        Disconnect a connected channel from one or more workspaces.
        https://api.slack.com/methods/admin.conversations.disconnectShared

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to be disconnected from some workspaces.
        :type str: e.g. C12345

        :param leaving_team_ids: The team to be removed from the channel. Currently only a single team id can be specified.
        :type str: e.g. T123, T4567

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.disconnect_shared(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        if leaving_team_ids is not None:
            payload["leaving_team_ids"] = leaving_team_ids

        return self._post(
            "admin.conversations.disconnectShared", payload=payload, **kwargs
        )

    def get_conversation_prefs(self, channel_id: str, **kwargs) -> Response:
        """
        Get conversation preferences for a public or private channel.
        https://api.slack.com/methods/admin.conversations.getConversationPrefs

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to get preferences for.
        :type str: e.g. C12345

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.get_conversation_prefs(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "channel_id": channel_id}

        return self._post(
            "admin.conversations.getConversationPrefs", payload=payload, **kwargs
        )

    def get_teams(
        self, channel_id: str, cursor: str = None, limit: int = None, **kwargs
    ) -> Response:
        """
        Get all the workspaces a given public or private channel is connected to within this Enterprise org.
        https://api.slack.com/methods/admin.conversations.getTeams

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to determine connected workspaces within the organization for.
        :type str: e.g. C12345

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page
        :type str: e.g. 5c3e53d5

        :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
        :type int: e.g. 100

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.get_teams(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "teams": "T1234,T5678"
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._post("admin.conversations.getTeams", payload=payload, **kwargs)

    def invite(self, channel_id: str, user_ids: str, **kwargs) -> Response:
        """
        Invite a user to a public or private channel.
        https://api.slack.com/methods/admin.conversations.invite

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel that the users will be invited to.
        :type str: e.g. C12345

        :param user_ids: The users to invite.
        :type str: e.g. U1234,U2345,U3456

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.invite(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id, "user_ids": user_ids}

        return self._post("admin.conversations.invite", payload=payload, **kwargs)

    def rename(self, channel_id: str, name: str, **kwargs) -> Response:
        """
        Rename a public or private channel.
        https://api.slack.com/methods/admin.conversations.rename

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to rename.
        :type str: e.g. C12345

        :param name: name to rename
        :type str: e.g. my-renamed-channel

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.rename(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id, "name": name}

        return self._post("admin.conversations.rename", payload=payload, **kwargs)

    def search(
        self,
        cursor: str = None,
        limit: int = None,
        query: str = None,
        search_channel_types: str = None,
        sort: str = None,
        sort_dir: str = None,
        team_ids: str = None,
        **kwargs
    ) -> Response:
        """
        Search for public or private channels in an Enterprise organization.
        https://api.slack.com/methods/admin.conversations.search

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page.
        :type str: e.g. dXNlcjpVMEc5V0ZYTlo=

        :param limit: Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.
        :type int: e.g. 20

        :param query: Name of the the channel to query by.
        :type str: e.g. announcement

        :param search_channel_types: The type of channel to include or exclude in the search. For example private will search private channels, while private_exclude will exclude them. For a full list of types, check the Types section.
        :type str: e.g. private,archived

        :param sort: Possible values are relevant (search ranking based on what we think is closest), name (alphabetical), member_count (number of users in the channel), and created (date channel was created). You can optionally pair this with the sort_dir arg to change how it is sorted
        :type str: e.g. name

        :param sort_dir: Sort direction. Possible values are asc for ascending order like (1, 2, 3) or (a, b, c), and desc for descending order like (3, 2, 1) or (c, b, a)
        :type str: e.g. asc

        :param team_ids: Comma separated string of team IDs, signifying the workspaces to search through.
        :type str: e.g. T00000000,T00000001

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.search(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if query is not None:
            payload["query"] = query

        if search_channel_types is not None:
            payload["search_channel_types"] = search_channel_types

        if sort is not None:
            payload["sort"] = sort

        if sort_dir is not None:
            payload["sort_dir"] = sort_dir

        if team_ids is not None:
            payload["team_ids"] = team_ids

        return self._post("admin.conversations.search", payload=payload, **kwargs)

    def set_conversation_prefs(self, channel_id: str, prefs: str, **kwargs) -> Response:
        """
        Set the posting permissions for a public or private channel.
        https://api.slack.com/methods/admin.conversations.setConversationPrefs

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to set the prefs for
        :type str: e.g. C1234

        :param prefs: The prefs for this channel in a stringified JSON format.
        :type str: e.g. {'who_can_post':'type:admin,user:U1234,subteam:S1234'}

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.set_conversation_prefs(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id, "prefs": prefs}

        return self._post(
            "admin.conversations.setConversationPrefs", payload=payload, **kwargs
        )

    def set_teams(
        self,
        channel_id: str,
        org_channel: bool = None,
        target_team_ids: str = None,
        team_id: str = None,
        **kwargs
    ) -> Response:
        """
        Set the workspaces in an Enterprise grid org that connect to a public or private channel.
        https://api.slack.com/methods/admin.conversations.setTeams

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The encoded channel_id to add or remove to workspaces.
        :type str: e.g. C1234

        :param org_channel: True if channel has to be converted to an org channel
        :type bool: e.g. true

        :param target_team_ids: A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.
        :type str: e.g. T1234,T5678,T9012,T3456

        :param team_id: The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.set_teams(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        if org_channel is not None:
            payload["org_channel"] = org_channel

        if target_team_ids is not None:
            payload["target_team_ids"] = target_team_ids

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.conversations.setTeams", payload=payload, **kwargs)

    def unarchive(self, channel_id: str, **kwargs) -> Response:
        """
        Unarchive a public or private channel.
        https://api.slack.com/methods/admin.conversations.unarchive

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_id: The channel to unarchive.
        :type str: e.g. C12345

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.conversations.unarchive(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_id": channel_id}

        return self._post("admin.conversations.unarchive", payload=payload, **kwargs)


class Emoji(SlackAPI):
    def add(self, name: str, url: str, **kwargs) -> Response:
        """
        Add an emoji.
        https://api.slack.com/methods/admin.emoji.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: The name of the emoji to be added. Colons (:myemoji:) around the value are not required, although they may be included.
        :type str: e.g. :helloworld:

        :param url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best.
        :type str: https://www.someimage.com/image-here.png

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.emoji.add(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "name": name, "url": url}

        return self._get("admin.emoji.add", payload=payload, **kwargs)

    def add_alias(self, alias_for: str, name: str, **kwargs) -> Response:
        """
        Add an emoji alias.
        https://api.slack.com/methods/admin.emoji.addAlias

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param alias_for: The alias of the emoji.
        :type str:

        :param name: The name of the emoji to be aliased. Colons (:myemoji:) around the value are not required, although they may be included.
        :type str: e.g. :helloworld:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.emoji.add_alias(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "alias_for": alias_for, "name": name}

        return self._get("admin.emoji.addAlias", payload=payload, **kwargs)

    def list(self, cursor: str = None, limit: int = None, **kwargs) -> Response:
        """
        List emoji for an Enterprise Grid organization.
        https://api.slack.com/methods/admin.emoji.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page
        :type str: e.g. 5c3e53d5

        :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
        :type int: e.g. 100

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.emoji.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "emoji": {
                "bowtie": "https://emoji.slack-edge.com/T9TK3CUKW/bowtie/f3ec6f2bb0.png",
                "squirrel": "https://emoji.slack-edge.com/T9TK3CUKW/squirrel/465f40c0e0.png",
                "glitch_crab": "https://emoji.slack-edge.com/T9TK3CUKW/glitch_crab/db049f1f9c.png",
                "piggy": "https://emoji.slack-edge.com/T9TK3CUKW/piggy/b7762ee8cd.png",
                "cubimal_chick": "https://emoji.slack-edge.com/T9TK3CUKW/cubimal_chick/85961c43d7.png",
                "dusty_stick": "https://emoji.slack-edge.com/T9TK3CUKW/dusty_stick/6177a62312.png",
                "slack": "https://emoji.slack-edge.com/T9TK3CUKW/slack/7d462d2443.png",
                "pride": "https://emoji.slack-edge.com/T9TK3CUKW/pride/56b1bd3388.png",
                "thumbsup_all": "https://emoji.slack-edge.com/T9TK3CUKW/thumbsup_all/50096a1020.gif",
                "slack_call": "https://emoji.slack-edge.com/T9TK3CUKW/slack_call/b81fffd6dd.png",
                "shipit": "alias:squirrel",
                "white_square": "alias:white_large_square",
                "black_square": "alias:black_large_square",
                "simple_smile": {
                    "apple": "https://a.slack-edge.com/80588/img/emoji_2017_12_06/apple/simple_smile.png",
                    "google": "https://a.slack-edge.com/80588/img/emoji_2017_12_06/google/simple_smile.png"
                }
            },
            "cache_ts": "1575283387.000000",
            "categories_version": "5",
            "categories": [
                {
                    "name": "Smileys & People",
                    "emoji_names": [
                        "grinning",
                        "grin",
                        "joy",
                        "etc etc ..."
                    ]
                }
            ]
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._get("admin.emoji.list", payload=payload, **kwargs)

    def remove(self, name: str, **kwargs) -> Response:
        """
        Remove an emoji across an Enterprise Grid organization
        https://api.slack.com/methods/admin.emoji.remove

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: The name of the emoji to be removed. Colons (:myemoji:) around the value are not required, although they may be included.
        :type str: :helloworld:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.emoji.remove(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "name": name}

        return self._get("admin.emoji.remove", payload=payload, **kwargs)

    def rename(self, name: str, new_name: str, **kwargs) -> Response:
        """
        Rename an emoji.
        https://api.slack.com/methods/admin.emoji.rename

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: The name of the emoji to be renamed. Colons (:myemoji:) around the value are not required, although they may be included.
        :type str: e.g. :helloworld:

        :param new_name: The new name of the emoji.
        :type str: e.g. :goodbyeworld:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.emoji.rename(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "name": name, "new_name": new_name}

        return self._get("admin.emoji.rename", payload=payload, **kwargs)


class Approved_(SlackAPI):
    """
    Renamed to conflict
    TODO: think of more elegant solution
    """

    def list(
        self, cursor: str = None, limit: int = None, team_id: str = None, **kwargs
    ) -> Response:
        """
        List all approved workspace invite requests.
        https://api.slack.com/methods/admin.inviteRequests.approved.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Value of the next_cursor field sent as part of the previous API response
        :type str: e.g. 5cweb43

        :param limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
        :type int: e.g. 100

        :param team_id: ID for the workspace where the invite requests were made.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.invite_requests.approved.list(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post(
            "admin.inviteRequests.approved.list", payload=payload, **kwargs
        )


class Denied(SlackAPI):
    def list(
        self, cursor: str = None, limit: int = None, team_id: str = None, **kwargs
    ) -> Response:
        """
        List all denied workspace invite requests.
        https://api.slack.com/methods/admin.inviteRequests.denied.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Value of the next_cursor field sent as part of the previous api response
        :type str: e.g. 5cweb43

        :param limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive
        :type int: e.g. 100

        :param team_id: ID for the workspace where the invite requests were made.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.invite_requests.denied.list(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.inviteRequests.denied.list", payload=payload, **kwargs)


class InviteRequests(SlackAPI):
    @cached_property
    def approved(self) -> Approved_:
        return Approved_(**self.params)

    @cached_property
    def denied(self) -> Denied:
        return Denied(**self.params)

    def approve(
        self, invite_request_id: str, team_id: str = None, **kwargs
    ) -> Response:
        """
        Approve a workspace invite request.
        https://api.slack.com/methods/admin.inviteRequests.approve

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param invite_request_id: ID of the request to invite.
        :type str: e.g. Ir1234

        :param team_id: ID for the workspace where the invite request was made.
        :type str: e.g. H34344

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.invite_requests.approve(**your_params)
        <Response [200]>
        >>> response.json()
            {
                "ok": true
            }

        """

        payload = {"token": self._token, "invite_request_id": invite_request_id}

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.inviteRequests.approve", payload=payload, **kwargs)

    def deny(self, invite_request_id: str, team_id: str = None, **kwargs) -> Response:
        """
        Deny a workspace invite request.
        https://api.slack.com/methods/admin.inviteRequests.deny

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param invite_request_id: ID of the request to invite.
        :type str: e.g. Ir1234

        :param team_id: ID for the workspace where the invite request was made.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.invite_requests.deny(**your_params)
        <Response [200]>
        >>> response.json()
            {
                "ok": true
            }
        """

        payload = {"token": self._token, "invite_request_id": invite_request_id}

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.inviteRequests.deny", payload=payload, **kwargs)

    def list(
        self, cursor: str = None, limit: int = None, team_id: str = None, **kwargs
    ) -> Response:
        """
        List all pending workspace invite requests.
        https://api.slack.com/methods/admin.inviteRequests.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Value of the next_cursor field sent as part of the previous API response
        :type str: e.g. 5cweb43

        :param limit: The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
        :type int: e.g. 100

        :param team_id: ID for the workspace where the invite requests were made.
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.invite_requests.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.inviteRequests.list", payload=payload, **kwargs)


class Admins(SlackAPI):
    def list(
        self, team_id: str, cursor: str = None, limit: int = None, **kwargs
    ) -> Response:
        """
        List all of the admins on a given workspace.
        https://api.slack.com/methods/admin.teams.admins.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page.
        :type str: e.g. dXNlcjpVMEc5V0ZYTlo=

        :param limit: The maximum number of items to return.
        :type int: e.g. 200

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.admins.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "admin_ids": [
                "U1234"
            ]
        }
        """

        payload = {"token": self._token, "team_id": team_id}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._get("admin.teams.admins.list", payload=payload, **kwargs)


class Owners(SlackAPI):
    def list(
        self, team_id: str, cursor: str = None, limit: int = None, **kwargs
    ) -> Response:
        """
        List all of the owners on a given workspace.
        https://api.slack.com/methods/admin.teams.owners.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page.
        :type str: e.g. 5c3e53d5

        :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
        :type int: e.g. 100

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.owners.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "owner_ids": [
                "U1234"
            ]
        }
        """

        payload = {"token": self._token, "team_id": team_id}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._get("admin.teams.owners.list", payload=payload, **kwargs)


class Settings(SlackAPI):
    def info(self, team_id: str, **kwargs) -> Response:
        """
        Fetch information about settings in a workspace
        https://api.slack.com/methods/admin.teams.settings.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.settings.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "team": {
                "id": "string",
                "name": "string",
                "domain": "string",
                "email_domain": "string",
                "icon": "array",
                "enterprise_id": "string",
                "enterprise_name": "string",
                "default_channels": "array"
            }
        }
        """

        payload = {"token": self._token, "team_id": team_id}

        return self._post("admin.teams.settings.info", payload=payload, **kwargs)

    def set_default_channels(
        self, channel_ids: str, team_id: str, **kwargs
    ) -> Response:
        """
        Set the default channels of a workspace.
        https://api.slack.com/methods/admin.teams.settings.setDefaultChannels

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_ids: An array of channel IDs.
        :type str:

        :param team_id: The id of the team
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.settings.set_default_channels(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "channel_ids": channel_ids, "team_id": team_id}

        return self._get(
            "admin.teams.settings.setDefaultChannels", payload=payload, **kwargs
        )

    def set_description(self, description: str, team_id: str, **kwargs) -> Response:
        """
        Set the description of a given workspace.
        https://api.slack.com/methods/admin.teams.settings.setDescription

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param description: The new description for the workspace.
        :type str:

        :param team_id: ID for the workspace to set the description for.
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.settings.set_description(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "description": description, "team_id": team_id}

        return self._post(
            "admin.teams.settings.setDescription", payload=payload, **kwargs
        )

    def set_discoverability(
        self, discoverability: str, team_id: str, **kwargs
    ) -> Response:
        """
        An API method that allows admins to set the discoverability of a given workspace
        https://api.slack.com/methods/admin.teams.settings.setDiscoverability

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param discoverability: This workspace's discovery setting. It must be set to one of open, invite_only, closed, or unlisted.
        :type str:

        :param team_id: The ID of the workspace to set discoverability on.
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.settings.set_discoverability(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "discoverability": discoverability,
            "team_id": team_id,
        }

        return self._post(
            "admin.teams.settings.setDiscoverability", payload=payload, **kwargs
        )

    def set_icon(self, image_url: str, team_id: str, **kwargs) -> Response:
        """
        Sets the icon of a workspace.
        https://api.slack.com/methods/admin.teams.settings.setIcon

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param image_url: Image URL for the icon
        :type str: e.g. http://mysite.com/icon.jpeg

        :param team_id: ID for the workspace to set the icon for.
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.settings.set_icon(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "image_url": image_url, "team_id": team_id}

        return self._get("admin.teams.settings.setIcon", payload=payload, **kwargs)

    def set_name(self, name: str, team_id: str, **kwargs) -> Response:
        """
        Set the name of a given workspace.
        https://api.slack.com/methods/admin.teams.settings.setName

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: The new name of the workspace.
        :type str:

        :param team_id: ID for the workspace to set the name for.
        :type str: e.g. T0HFE6EBT

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.settings.set_name(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "name": name, "team_id": team_id}

        return self._post("admin.teams.settings.setName", payload=payload, **kwargs)


class Teams(SlackAPI):
    @cached_property
    def admins(self) -> Admins:
        return Admins(**self.params)

    @cached_property
    def owners(self) -> Owners:
        return Owners(**self.params)

    @cached_property
    def settings(self) -> Settings:
        return Settings(**self.params)

    def create(
        self,
        team_domain: str,
        team_name: str,
        team_description: str = None,
        team_discoverability: str = None,
        **kwargs
    ) -> Response:
        """
        Create an Enterprise team.
        https://api.slack.com/methods/admin.teams.create

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_domain: Team domain (for example, slacksoftballteam).
        :type str:

        :param team_name: Team name (for example, Slack Softball Team).
        :type str:

        :param team_description: Description for the team.
        :type str:

        :param team_discoverability: Who can join the team. A team's discoverability can be open, closed, invite_only, or unlisted.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.create(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "team": "T12345"
        }
        """

        payload = {
            "token": self._token,
            "team_domain": team_domain,
            "team_name": team_name,
        }

        if team_description is not None:
            payload["team_description"] = team_description

        if team_discoverability is not None:
            payload["team_discoverability"] = team_discoverability

        return self._post("admin.teams.create", payload=payload, **kwargs)

    def list(self, cursor: str = None, limit: int = None, **kwargs) -> Response:
        """
        List all teams on an Enterprise organization
        https://api.slack.com/methods/admin.teams.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page.
        :type str: e.g. 5c3e53d5

        :param limit: The maximum number of items to return. Must be between 1 - 100 both inclusive.
        :type int: e.g. 50

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.teams.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "teams": [
                {
                    "id": "T1234",
                    "name": "My Team",
                    "discoverability": "hidden",
                    "primary_owner": {
                        "user_id": "W1234",
                        "email": "bront@slack.com"
                    },
                    "team_url": "https://subarachnoid.slack.com/"
                }
            ]
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._post("admin.teams.list", payload=payload, **kwargs)


class Usergroups(SlackAPI):
    def add_channels(
        self, channel_ids: str, usergroup_id: str, team_id: str = None, **kwargs
    ) -> Response:
        """
        Add one or more default channels to an IDP group.
        https://api.slack.com/methods/admin.usergroups.addChannels

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_ids: Comma separated string of channel IDs.
        :type str: e.g. C00000000,C00000001

        :param usergroup_id: ID of the IDP group to add default channels for.
        :type str: e.g. S00000000

        :param team_id: The workspace to add default channels in.
        :type str: e.g. T00000000

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.usergroups.add_channels(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "channel_ids": channel_ids,
            "usergroup_id": usergroup_id,
        }

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.usergroups.addChannels", payload=payload, **kwargs)

    def add_teams(
        self, team_ids: str, usergroup_id: str, auto_provision: bool = None, **kwargs
    ) -> Response:
        """
        Associate one or more default workspaces with an organization-wide IDP group.
        https://api.slack.com/methods/admin.usergroups.addTeams

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_ids: A comma separated list of encoded team (workspace) IDs. Each workspace MUST belong to the organization associated with the token.
        :type str: e.g. T12345678,T98765432

        :param usergroup_id: An encoded usergroup (IDP Group) ID.
        :type str: e.g. S12345678

        :param auto_provision: When true, this method automatically creates new workspace accounts for the IDP group members.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.usergroups.add_teams(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "team_ids": team_ids,
            "usergroup_id": usergroup_id,
        }

        if auto_provision is not None:
            payload["auto_provision"] = auto_provision

        return self._post("admin.usergroups.addTeams", payload=payload, **kwargs)

    def list_channels(
        self,
        usergroup_id: str,
        include_num_members: bool = None,
        team_id: str = None,
        **kwargs
    ) -> Response:
        """
        List the channels linked to an org-level IDP group (user group).
        https://api.slack.com/methods/admin.usergroups.listChannels

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param usergroup_id: ID of the IDP group to list default channels for.
        :type str: e.g. S00000000

        :param include_num_members: Flag to include or exclude the count of members per channel.
        :type bool: e.g. true

        :param team_id: ID of the the workspace.
        :type str: e.g. T00000000

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.usergroups.list_channels(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "channels": [
                {
                    "id": "C024BE91L",
                    "name": "fun",
                    "team_id": "T024BE911",
                    "num_members": 34
                },
                {
                    "id": "C024BE91K",
                    "name": "more fun",
                    "team_id": "T024BE912"
                },
                {
                    "id": "C024BE91M",
                    "name": "public-channel",
                    "team_id": "T024BE911",
                    "is_redacted": true,
                    "num_members": 34
                },
                {
                    "id": "C024BE91N",
                    "name": "some more fun",
                    "team_id": "T024BE921"
                }
            ]
        }
        """

        payload = {"token": self._token, "usergroup_id": usergroup_id}

        if include_num_members is not None:
            payload["include_num_members"] = include_num_members

        if team_id is not None:
            payload["team_id"] = team_id

        return self._post("admin.usergroups.listChannels", payload=payload, **kwargs)

    def remove_channels(
        self, channel_ids: str, usergroup_id: str, **kwargs
    ) -> Response:
        """
        Remove one or more default channels from an org-level IDP group (user group).
        https://api.slack.com/methods/admin.usergroups.removeChannels

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_ids: Comma-separated string of channel IDs
        :type str: e.g. C00000000,C00000001

        :param usergroup_id: ID of the IDP Group
        :type str: e.g. S00000000

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.usergroups.remove_channels(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "channel_ids": channel_ids,
            "usergroup_id": usergroup_id,
        }

        return self._post("admin.usergroups.removeChannels", payload=payload, **kwargs)


class Session(SlackAPI):
    def reset(
        self, user_id: str, mobile_only: bool = None, web_only: bool = None, **kwargs
    ) -> Response:
        """
        Wipes all valid sessions on all devices for a given user
        https://api.slack.com/methods/admin.users.session.reset

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param user_id: The ID of the user to wipe sessions for
        :type str: e.g. W12345678

        :param mobile_only: Only expire mobile sessions (default: false)
        :type bool: e.g. true

        :param web_only: Only expire web sessions (default: false)
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.session.reset(**your_params)
        <Response [200]>
        >>> response.json()
        {
          "token": "xoxp-xxxxxxxx-xxxxxxxx",
          "user_id": "U1234",
          "mobile_only": true
        }

        """

        payload = {"token": self._token, "user_id": user_id}

        if mobile_only is not None:
            payload["mobile_only"] = mobile_only

        if web_only is not None:
            payload["web_only"] = web_only

        return self._post("admin.users.session.reset", payload=payload, **kwargs)


class Users(SlackAPI):
    @cached_property
    def session(self) -> Session:
        return Session(**self.params)

    def assign(
        self,
        team_id: str,
        user_id: str,
        channel_ids: str = None,
        is_restricted: bool = None,
        is_ultra_restricted: bool = None,
        **kwargs
    ) -> Response:
        """
        Add an Enterprise user to a workspace.
        https://api.slack.com/methods/admin.users.assign

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param user_id: The ID of the user to add to the workspace.
        :type str:

        :param channel_ids: Comma separated values of channel IDs to add user in the new workspace.
        :type str: e.g. C123,C3456

        :param is_restricted: True if user should be added to the workspace as a guest.
        :type bool: e.g. true

        :param is_ultra_restricted: True if user should be added to the workspace as a single-channel guest.
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.assign(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "team_id": team_id, "user_id": user_id}

        if channel_ids is not None:
            payload["channel_ids"] = channel_ids

        if is_restricted is not None:
            payload["is_restricted"] = is_restricted

        if is_ultra_restricted is not None:
            payload["is_ultra_restricted"] = is_ultra_restricted

        return self._post("admin.users.assign", payload=payload, **kwargs)

    def invite(
        self,
        channel_ids: str,
        email: str,
        team_id: str,
        custom_message: str = None,
        guest_expiration_ts: float = None,
        is_restricted: bool = None,
        is_ultra_restricted: bool = None,
        real_name: str = None,
        resend: bool = None,
        **kwargs
    ) -> Response:
        """
        Invite a user to a workspace.
        https://api.slack.com/methods/admin.users.invite

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel_ids: A comma-separated list of channel_ids for this user to join. At least one channel is required.
        :type str: e.g. C1A2B3C4D,C26Z25Y24

        :param email: The email address of the person to invite.
        :type str: e.g. joe@email.com

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param custom_message: An optional message to send to the user in the invite email.
        :type str: e.g. Come and join our team!

        :param guest_expiration_ts: Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.
        :type float: e.g. 0123456789.012345

        :param is_restricted: Is this user a multi-channel guest user? (default: false)
        :type bool: e.g. true

        :param is_ultra_restricted: Is this user a single channel guest user? (default: false)
        :type bool: e.g. true

        :param real_name: Full name of the user.
        :type str: e.g. {"full_name":"Joe Smith"}

        :param resend: Allow this invite to be resent in the future if a user has not signed up yet. (default: false)
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.invite(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "channel_ids": channel_ids,
            "email": email,
            "team_id": team_id,
        }

        if custom_message is not None:
            payload["custom_message"] = custom_message

        if guest_expiration_ts is not None:
            payload["guest_expiration_ts"] = guest_expiration_ts

        if is_restricted is not None:
            payload["is_restricted"] = is_restricted

        if is_ultra_restricted is not None:
            payload["is_ultra_restricted"] = is_ultra_restricted

        if real_name is not None:
            payload["real_name"] = real_name

        if resend is not None:
            payload["resend"] = resend

        return self._post("admin.users.invite", payload=payload, **kwargs)

    def list(
        self, team_id: str, cursor: str = None, limit: int = None, **kwargs
    ) -> Response:
        """
        List users on a workspace
        https://api.slack.com/methods/admin.users.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param cursor: Set cursor to next_cursor returned by the previous call to list items in the next page.
        :type str: e.g. 5c3e53d5

        :param limit: Limit for how many users to be retrieved per page
        :type int: e.g. 50

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "users": [
                {
                    "id": "T1234",
                    "email": "bront@slack.com",
                    "is_admin": false,
                    "is_owner": false,
                    "is_primary_owner": false,
                    "is_restricted": false,
                    "is_ultra_restricted": false,
                    "is_bot": false
                }
            ]
        }
        """

        payload = {"token": self._token, "team_id": team_id}

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        return self._post("admin.users.list", payload=payload, **kwargs)

    def remove(self, team_id: str, user_id: str, **kwargs) -> Response:
        """
        Remove a user from a workspace.
        https://api.slack.com/methods/admin.users.remove

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param user_id: The ID of the user to remove.
        :type str: e.g. W12345678

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.remove(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "team_id": team_id, "user_id": user_id}

        return self._post("admin.users.remove", payload=payload, **kwargs)

    def set_admin(self, team_id: str, user_id: str, **kwargs) -> Response:
        """
        Set an existing guest, regular user, or owner to be an admin user.
        https://api.slack.com/methods/admin.users.setAdmin

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param user_id: The ID of the user to designate as an admin.
        :type str: e.g. W12345678

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.set_admin(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "team_id": team_id, "user_id": user_id}

        return self._post("admin.users.setAdmin", payload=payload, **kwargs)

    def set_expiration(
        self, expiration_ts: int, team_id: str, user_id: str, **kwargs
    ) -> Response:
        """
        Set an expiration for a guest user
        https://api.slack.com/methods/admin.users.setExpiration

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param expiration_ts: Timestamp when guest account should be disabled.
        :type int: e.g. 1234567890

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param user_id: The ID of the user to set an expiration for.
        :type str: e.g. W12345678

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.set_expiration(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {
            "token": self._token,
            "expiration_ts": expiration_ts,
            "team_id": team_id,
            "user_id": user_id,
        }

        return self._post("admin.users.setExpiration", payload=payload, **kwargs)

    def set_owner(self, team_id: str, user_id: str, **kwargs) -> Response:
        """
        Set an existing guest, regular user, or admin user to be a workspace owner.
        https://api.slack.com/methods/admin.users.setOwner

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param user_id: Id of the user to promote to owner.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.set_owner(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "team_id": team_id, "user_id": user_id}

        return self._post("admin.users.setOwner", payload=payload, **kwargs)

    def set_regular(self, team_id: str, user_id: str, **kwargs) -> Response:
        """
        Set an existing guest user, admin user, or owner to be a regular user.
        https://api.slack.com/methods/admin.users.setRegular

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param team_id: The ID (T1234) of the workspace.
        :type str: e.g. T1234

        :param user_id: The ID of the user to designate as a regular user.
        :type str: e.g. W12345678

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.admin.users.set_regular(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "team_id": team_id, "user_id": user_id}

        return self._post("admin.users.setRegular", payload=payload, **kwargs)


class Admin(SlackAPI):
    @cached_property
    def apps(self) -> Apps:
        return Apps(**self.params)

    @cached_property
    def conversations(self) -> Conversations:
        return Conversations(**self.params)

    @cached_property
    def emoji(self) -> Emoji:
        return Emoji(**self.params)

    @cached_property
    def invite_requests(self) -> InviteRequests:
        return InviteRequests(**self.params)

    @cached_property
    def teams(self) -> Teams:
        return Teams(**self.params)

    @cached_property
    def usergroups(self) -> Usergroups:
        return Usergroups(**self.params)

    @cached_property
    def users(self) -> Users:
        return Users(**self.params)
