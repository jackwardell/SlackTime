# -*- coding: utf-8 -*-
from typing import IO
from typing import Union

from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property
from slack_time.utils import make_file


class Profile(SlackAPI):
    def get(self, include_labels: bool = None, user: str = None, **kwargs) -> Response:
        """
        Retrieves a user's profile information.
        https://api.slack.com/methods/users.profile.get

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param include_labels: Include labels for each ID in custom profile fields
        :type bool: e.g. true

        :param user: User to retrieve profile info for
        :type str: e.g. W1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.profile.get(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "profile": {
                "avatar_hash": "ge3b51ca72de",
                "status_text": "Print is dead",
                "status_emoji": ":books:",
                "status_expiration": 0,
                "real_name": "Egon Spengler",
                "display_name": "spengler",
                "real_name_normalized": "Egon Spengler",
                "display_name_normalized": "spengler",
                "email": "spengler@ghostbusters.example.com",
                "image_original": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_24": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_32": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_48": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_72": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_192": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_512": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "team": "T012AB3C4"
            }
        }
        """

        payload = {"token": self._token}

        if include_labels is not None:
            payload["include_labels"] = include_labels

        if user is not None:
            payload["user"] = user

        return self._get("users.profile.get", payload=payload, **kwargs)

    def set(
        self,
        name: str = None,
        profile: dict = None,
        user: str = None,
        value: str = None,
        **kwargs
    ) -> Response:
        """
        Set the profile information for a user.
        https://api.slack.com/methods/users.profile.set

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param name: Name of a single key to set. Usable only if profile is not passed.
        :type str: e.g. first_name

        :param profile: Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.
        :type dict: e.g. { first_name: "John", ... }

        :param user: ID of user to change. This argument may only be specified by team admins on paid teams.
        :type str: e.g. W1234567890

        :param value: Value to set a single key to. Usable only if profile is not passed.
        :type str: e.g. John

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.profile.set(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "profile": {
                "avatar_hash": "ge3b51ca72de",
                "status_text": "Print is dead",
                "status_emoji": ":books:",
                "status_expiration": 0,
                "real_name": "Egon Spengler",
                "display_name": "spengler",
                "real_name_normalized": "Egon Spengler",
                "display_name_normalized": "spengler",
                "email": "spengler@ghostbusters.example.com",
                "image_24": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_32": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_48": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_72": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_192": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "image_512": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                "team": "T012AB3C4"
            }
        }
        """

        payload = {"token": self._token}

        if name is not None:
            payload["name"] = name

        if profile is not None:
            payload["profile"] = profile

        if user is not None:
            payload["user"] = user

        if value is not None:
            payload["value"] = value

        return self._post("users.profile.set", payload=payload, **kwargs)


class Users(SlackAPI):
    @cached_property
    def profile(self) -> Profile:
        return Profile(**self.params)

    def conversations(
        self,
        cursor: str = None,
        exclude_archived: bool = None,
        limit: int = None,
        types: str = None,
        user: str = None,
        **kwargs
    ) -> Response:
        """
        List conversations the calling user may access.
        https://api.slack.com/methods/users.conversations

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param exclude_archived: Set to true to exclude archived channels from the list
        :type bool: e.g. true

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.
        :type int: e.g. 20

        :param types: Mix and match channel types by providing a comma-separated list of any combination of public_channel, private_channel, mpim, im
        :type str: e.g. im,mpim

        :param user: Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership.
        :type str: e.g. W0B2345D

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.conversations(**your_params)
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
                    "previous_names": []
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
                    "previous_names": []
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

        if user is not None:
            payload["user"] = user

        return self._get("users.conversations", payload=payload, **kwargs)

    def delete_photo(self, **kwargs) -> Response:
        """
        Delete the user profile photo
        https://api.slack.com/methods/users.deletePhoto

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.delete_photo(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token}

        return self._get("users.deletePhoto", payload=payload, **kwargs)

    def get_presence(self, user: str = None, **kwargs) -> Response:
        """
        Gets user presence information.
        https://api.slack.com/methods/users.getPresence

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param user: User to get presence info on. Defaults to the authed user.
        :type str: e.g. W1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.get_presence(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "presence": "active"
        }
        """

        payload = {"token": self._token}

        if user is not None:
            payload["user"] = user

        return self._get("users.getPresence", payload=payload, **kwargs)

    def identity(self, **kwargs) -> Response:
        """
        Get a user's identity.
        https://api.slack.com/methods/users.identity

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.identity(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "user": {
                "name": "Sonny Whether",
                "id": "U0G9QF9C6"
            },
            "team": {
                "id": "T0G9PQBBK"
            }
        }
        """

        payload = {"token": self._token}

        return self._get("users.identity", payload=payload, **kwargs)

    def info(self, user: str, include_locale: bool = None, **kwargs) -> Response:
        """
        Gets information about a user.
        https://api.slack.com/methods/users.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param user: User to get info on
        :type str: e.g. W1234567890

        :param include_locale: Set this to true to receive the locale for this user. Defaults to false
        :type bool: e.g. true

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "user": {
                "id": "W012A3CDE",
                "team_id": "T012AB3C4",
                "name": "spengler",
                "deleted": false,
                "color": "9f69e7",
                "real_name": "Egon Spengler",
                "tz": "America/Los_Angeles",
                "tz_label": "Pacific Daylight Time",
                "tz_offset": -25200,
                "profile": {
                    "avatar_hash": "ge3b51ca72de",
                    "status_text": "Print is dead",
                    "status_emoji": ":books:",
                    "real_name": "Egon Spengler",
                    "display_name": "spengler",
                    "real_name_normalized": "Egon Spengler",
                    "display_name_normalized": "spengler",
                    "email": "spengler@ghostbusters.example.com",
                    "image_original": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_24": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_32": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_48": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_72": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_192": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_512": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "team": "T012AB3C4"
                },
                "is_admin": true,
                "is_owner": false,
                "is_primary_owner": false,
                "is_restricted": false,
                "is_ultra_restricted": false,
                "is_bot": false,
                "updated": 1502138686,
                "is_app_user": false,
                "has_2fa": false
            }
        }
        """

        payload = {"token": self._token, "user": user}

        if include_locale is not None:
            payload["include_locale"] = include_locale

        return self._get("users.info", payload=payload, **kwargs)

    def list(
        self,
        cursor: str = None,
        include_locale: bool = None,
        limit: int = None,
        **kwargs
    ) -> Response:
        """
        Lists all users in a Slack team.
        https://api.slack.com/methods/users.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param include_locale: Set this to true to receive the locale for users. Defaults to false
        :type bool: e.g. true

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached. Providing no limit value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience limit_required or HTTP 500 errors.
        :type int: e.g. 20

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "members": [
                {
                    "id": "W012A3CDE",
                    "team_id": "T012AB3C4",
                    "name": "spengler",
                    "deleted": false,
                    "color": "9f69e7",
                    "real_name": "spengler",
                    "tz": "America/Los_Angeles",
                    "tz_label": "Pacific Daylight Time",
                    "tz_offset": -25200,
                    "profile": {
                        "avatar_hash": "ge3b51ca72de",
                        "status_text": "Print is dead",
                        "status_emoji": ":books:",
                        "real_name": "Egon Spengler",
                        "display_name": "spengler",
                        "real_name_normalized": "Egon Spengler",
                        "display_name_normalized": "spengler",
                        "email": "spengler@ghostbusters.example.com",
                        "image_24": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                        "image_32": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                        "image_48": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                        "image_72": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                        "image_192": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                        "image_512": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                        "team": "T012AB3C4"
                    },
                    "is_admin": true,
                    "is_owner": false,
                    "is_primary_owner": false,
                    "is_restricted": false,
                    "is_ultra_restricted": false,
                    "is_bot": false,
                    "updated": 1502138686,
                    "is_app_user": false,
                    "has_2fa": false
                },
                {
                    "id": "W07QCRPA4",
                    "team_id": "T0G9PQBBK",
                    "name": "glinda",
                    "deleted": false,
                    "color": "9f69e7",
                    "real_name": "Glinda Southgood",
                    "tz": "America/Los_Angeles",
                    "tz_label": "Pacific Daylight Time",
                    "tz_offset": -25200,
                    "profile": {
                        "avatar_hash": "8fbdd10b41c6",
                        "image_24": "https://a.slack-edge.com...png",
                        "image_32": "https://a.slack-edge.com...png",
                        "image_48": "https://a.slack-edge.com...png",
                        "image_72": "https://a.slack-edge.com...png",
                        "image_192": "https://a.slack-edge.com...png",
                        "image_512": "https://a.slack-edge.com...png",
                        "image_1024": "https://a.slack-edge.com...png",
                        "image_original": "https://a.slack-edge.com...png",
                        "first_name": "Glinda",
                        "last_name": "Southgood",
                        "title": "Glinda the Good",
                        "phone": "",
                        "skype": "",
                        "real_name": "Glinda Southgood",
                        "real_name_normalized": "Glinda Southgood",
                        "display_name": "Glinda the Fairly Good",
                        "display_name_normalized": "Glinda the Fairly Good",
                        "email": "glenda@south.oz.coven"
                    },
                    "is_admin": true,
                    "is_owner": false,
                    "is_primary_owner": false,
                    "is_restricted": false,
                    "is_ultra_restricted": false,
                    "is_bot": false,
                    "updated": 1480527098,
                    "has_2fa": false
                }
            ],
            "cache_ts": 1498777272,
            "response_metadata": {
                "next_cursor": "dXNlcjpVMEc5V0ZYTlo="
            }
        }
        """

        payload = {"token": self._token}

        if cursor is not None:
            payload["cursor"] = cursor

        if include_locale is not None:
            payload["include_locale"] = include_locale

        if limit is not None:
            payload["limit"] = limit

        return self._get("users.list", payload=payload, **kwargs)

    def lookup_by_email(self, email: str, **kwargs) -> Response:
        """
        Find a user with an email address.
        https://api.slack.com/methods/users.lookupByEmail

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param email: An email address belonging to a user in the workspace
        :type str: e.g. spengler@ghostbusters.example.com

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.lookup_by_email(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "user": {
                "id": "W012A3CDE",
                "team_id": "T012AB3C4",
                "name": "spengler",
                "deleted": false,
                "color": "9f69e7",
                "real_name": "Egon Spengler",
                "tz": "America/Los_Angeles",
                "tz_label": "Pacific Daylight Time",
                "tz_offset": -25200,
                "profile": {
                    "avatar_hash": "ge3b51ca72de",
                    "status_text": "Print is dead",
                    "status_emoji": ":books:",
                    "real_name": "Egon Spengler",
                    "display_name": "spengler",
                    "real_name_normalized": "Egon Spengler",
                    "display_name_normalized": "spengler",
                    "email": "spengler@ghostbusters.example.com",
                    "image_24": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_32": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_48": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_72": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_192": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "image_512": "https://.../avatar/e3b51ca72dee4ef87916ae2b9240df50.jpg",
                    "team": "T012AB3C4"
                },
                "is_admin": true,
                "is_owner": false,
                "is_primary_owner": false,
                "is_restricted": false,
                "is_ultra_restricted": false,
                "is_bot": false,
                "updated": 1502138686,
                "is_app_user": false,
                "has_2fa": false
            }
        }
        """

        payload = {"token": self._token, "email": email}

        return self._get("users.lookupByEmail", payload=payload, **kwargs)

    def set_active(self, **kwargs) -> Response:
        """
        Marked a user as active. Deprecated and non-functional.
        https://api.slack.com/methods/users.setActive

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.set_active(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        return self._post("users.setActive", payload=payload, **kwargs)

    def set_photo(
        self,
        crop_w: int = None,
        crop_x: int = None,
        crop_y: int = None,
        image: Union[str, IO] = None,
        **kwargs
    ) -> Response:
        """
        Set the user profile photo
        https://api.slack.com/methods/users.setPhoto

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param crop_w: Width/height of crop box (always square)
        :type int: e.g. 100

        :param crop_x: X coordinate of top-left corner of crop box
        :type int: e.g. 10

        :param crop_y: Y coordinate of top-left corner of crop box
        :type int: e.g. 15

        :param image: File contents via multipart/form-data.
        :type Union[str, IO]: e.g. '/absolute/path/to/file' or actual IO file"

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.set_photo(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if crop_w is not None:
            payload["crop_w"] = crop_w

        if crop_x is not None:
            payload["crop_x"] = crop_x

        if crop_y is not None:
            payload["crop_y"] = crop_y

        if image is not None:
            file_to_upload = make_file(image)
            kwargs["files"] = {"file": file_to_upload}

        return self._post("users.setPhoto", payload=payload, **kwargs)

    def set_presence(self, presence: str, **kwargs) -> Response:
        """
        Manually sets user presence.
        https://api.slack.com/methods/users.setPresence

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param presence: Either auto or away
        :type str: e.g. away

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.users.set_presence(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "presence": presence}

        return self._post("users.setPresence", payload=payload, **kwargs)
