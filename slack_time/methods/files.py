# -*- coding: utf-8 -*-
from typing import IO
from typing import Union

from requests import Response

from slack_time.api import SlackAPI
from slack_time.utils import cached_property
from slack_time.utils import make_file


class Comments(SlackAPI):
    def delete(self, file: str, id: str, **kwargs) -> Response:
        """
        Deletes an existing comment on a file.
        https://api.slack.com/methods/files.comments.delete

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param file: File to delete a comment from.
        :type str: e.g. F1234567890

        :param id: The comment to delete.
        :type str: e.g. Fc1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.comments.delete(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true
        }
        """

        payload = {"token": self._token, "file": file, "id": id}

        return self._post("files.comments.delete", payload=payload, **kwargs)


class Remote(SlackAPI):
    def add(
        self,
        external_id: int,
        external_url: str,
        title: str,
        filetype: str = None,
        indexable_file_contents: Union[str, IO] = None,
        preview_image: Union[str, IO] = None,
        **kwargs
    ) -> Response:
        """
        Adds a file from a remote service
        https://api.slack.com/methods/files.remote.add

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param external_id: Creator defined GUID for the file.
        :type int: e.g. 123456

        :param external_url: URL of the remote file.
        :type str: e.g. http://example.com/my_cloud_service_file/abc123

        :param title: Title of the file being shared.
        :type str: e.g. Danger, High Voltage!

        :param filetype: type of file
        :type str: e.g. doc

        :param indexable_file_contents: A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.
        :type Union[str, IO]: e.g. '/absolute/path/to/file' or actual IO file"

        :param preview_image: Preview of the document via multipart/form-data.
        :type Union[str, IO]: e.g. '/absolute/path/to/file' or actual IO file"

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.remote.add(**your_params)
        <Response [200]>
        >>> response.json()
            {
                "ok": true,
                "file": {
                    "id": "F0GDJ3XMH",
                    "created": 1563919925,
                    "timestamp": 1563919925,
                    "name": "LeadvilleAndBackAgain",
                    "title": "LeadvilleAndBackAgain",
                    "mimetype": "application/vnd.slack-remote",
                    "filetype": "remote",
                    "pretty_type": "Remote",
                    "user": "U0F8RBVNF",
                    "editable": false,
                    "size": 0,
                    "mode": "external",
                    "is_external": true,
                    "external_type": "app",
                    "is_public": false,
                    "public_url_shared": false,
                    "display_as_bot": false,
                    "username": "",
                    "url_private": "https://docs.google.com/document/d/1TA9fIaph4eSz2fC_1JGMuYaYUc4IvieIop0WqfCXw5Y/edit?usp=sharing",
                    "permalink": "https://kraneflannel.slack.com/files/U0F8RBVNF/F0GDJ3XMH/leadvilleandbackagain",
                    "comments_count": 0,
                    "is_starred": false,
                    "shares": {},
                    "channels": [],
                    "groups": [],
                    "ims": [],
                    "external_id": "1234",
                    "external_url": "https://docs.google.com/document/d/1TA9fIaph4eSz2fC_1JGMuYaYUc4IvieIop0WqfCXw5Y/edit?usp=sharing",
                    "has_rich_preview": false
                }
            }

        """

        payload = {
            "token": self._token,
            "external_id": external_id,
            "external_url": external_url,
            "title": title,
        }

        if filetype is not None:
            payload["filetype"] = filetype

        if indexable_file_contents is not None:
            file_to_upload = make_file(indexable_file_contents)
            payload["indexable_file_contents"] = file_to_upload

        if preview_image is not None:
            file_to_upload = make_file(indexable_file_contents)
            kwargs["files"] = {"file": file_to_upload}

        return self._get("files.remote.add", payload=payload, **kwargs)

    def info(self, external_id: int = None, file: str = None, **kwargs) -> Response:
        """
        Retrieve information about a remote file added to Slack
        https://api.slack.com/methods/files.remote.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param external_id: Creator defined GUID for the file.
        :type int: e.g. 123456

        :param file: Specify a file by providing its ID.
        :type str: e.g. F2147483862

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.remote.info(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if external_id is not None:
            payload["external_id"] = external_id

        if file is not None:
            payload["file"] = file

        return self._get("files.remote.info", payload=payload, **kwargs)

    def list(
        self,
        channel: str = None,
        cursor: str = None,
        limit: int = None,
        ts_from: int = None,
        ts_to: int = None,
        **kwargs
    ) -> Response:
        """
        Retrieve information about a remote file added to Slack
        https://api.slack.com/methods/files.remote.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Filter files appearing in a specific channel, indicated by its ID.
        :type str: e.g. C1234567890

        :param cursor: Paginate through collections of data by setting the cursor parameter to a next_cursor attribute returned by a previous request's response_metadata. Default value fetches the first "page" of the collection. See pagination for more detail.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param limit: The maximum number of items to return.
        :type int: e.g. 20

        :param ts_from: Filter files created after this timestamp (inclusive).
        :type int: e.g. 123456789

        :param ts_to: Filter files created before this timestamp (inclusive).
        :type int: e.g. 123456789

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.remote.list(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if channel is not None:
            payload["channel"] = channel

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if ts_from is not None:
            payload["ts_from"] = ts_from

        if ts_to is not None:
            payload["ts_to"] = ts_to

        return self._get("files.remote.list", payload=payload, **kwargs)

    def remove(self, external_id: int = None, file: str = None, **kwargs) -> Response:
        """
        Remove a remote file.
        https://api.slack.com/methods/files.remote.remove

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param external_id: Creator defined GUID for the file.
        :type int: e.g. 123456

        :param file: Specify a file by providing its ID.
        :type str: e.g. F2147483862

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.remote.remove(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if external_id is not None:
            payload["external_id"] = external_id

        if file is not None:
            payload["file"] = file

        return self._get("files.remote.remove", payload=payload, **kwargs)

    def share(
        self, channels: str, external_id: int = None, file: str = None, **kwargs
    ) -> Response:
        """
        Share a remote file into a channel.
        https://api.slack.com/methods/files.remote.share

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channels: Comma-separated list of channel IDs where the file will be shared.
        :type str: e.g. C1234567890,C2345678901,C3456789012

        :param external_id: The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or file or both are required.
        :type int: e.g. 123456

        :param file: Specify a file registered with Slack by providing its ID. Either this field or external_id or both are required.
        :type str: e.g. F2147483862

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.remote.share(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "channels": channels}

        if external_id is not None:
            payload["external_id"] = external_id

        if file is not None:
            payload["file"] = file

        return self._get("files.remote.share", payload=payload, **kwargs)

    def update(
        self,
        external_id: int = None,
        external_url: str = None,
        file: str = None,
        filetype: str = None,
        indexable_file_contents: Union[str, IO] = None,
        preview_image: Union[str, IO] = None,
        title: str = None,
        **kwargs
    ) -> Response:
        """
        Updates an existing remote file.
        https://api.slack.com/methods/files.remote.update

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param external_id: Creator defined GUID for the file.
        :type int: e.g. 123456

        :param external_url: URL of the remote file.
        :type str: e.g. http://example.com/my_cloud_service_file/abc123

        :param file: Specify a file by providing its ID.
        :type str: e.g. F2147483862

        :param filetype: type of file
        :type str: e.g. doc

        :param indexable_file_contents: File containing contents that can be used to improve searchability for the remote file.
        :type Union[str, IO]: e.g. '/absolute/path/to/file' or actual IO file"

        :param preview_image: Preview of the document via multipart/form-data.
        :type Union[str, IO]: e.g. '/absolute/path/to/file' or actual IO file"

        :param title: Title of the file being shared.
        :type str: e.g. Danger, High Voltage!

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.remote.update(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token}

        if external_id is not None:
            payload["external_id"] = external_id

        if external_url is not None:
            payload["external_url"] = external_url

        if file is not None:
            payload["file"] = file

        if filetype is not None:
            payload["filetype"] = filetype

        if indexable_file_contents is not None:
            file_to_upload = make_file(file)
            payload["indexable_file_contents"] = file_to_upload

        if preview_image is not None:
            file_to_upload = make_file(file)
            kwargs["files"] = {"file": file_to_upload}

        if title is not None:
            payload["title"] = title

        return self._get("files.remote.update", payload=payload, **kwargs)


class Files(SlackAPI):
    @cached_property
    def comments(self) -> Comments:
        return Comments(**self.params)

    @cached_property
    def remote(self) -> Remote:
        return Remote(**self.params)

    def delete(self, file: str, **kwargs) -> Response:
        """
        Deletes a file.
        https://api.slack.com/methods/files.delete

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param file: ID of file to delete.
        :type str: e.g. F1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.delete(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "file": file}

        return self._post("files.delete", payload=payload, **kwargs)

    def info(
        self,
        file: str,
        count: int = None,
        cursor: str = None,
        limit: int = None,
        page: int = None,
        **kwargs
    ) -> Response:
        """
        Gets information about a file.
        https://api.slack.com/methods/files.info

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param file: Specify a file by providing its ID.
        :type str: e.g. F2147483862

        :param count: Number of items to return per page.
        :type int: e.g. 20

        :param cursor: Parameter for pagination. File comments are paginated for a single file. Set cursor equal to the next_cursor attribute returned by the previous request's response_metadata. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection of comments. See pagination for more details.
        :type str: e.g. dXNlcjpVMDYxTkZUVDI=

        :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
        :type int: e.g. 20

        :param page: Page number of results to return.
        :type int: e.g. 2

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.info(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "file": {
                "id": "F0S43PZDF",
                "created": 1531763342,
                "timestamp": 1531763342,
                "name": "tedair.gif",
                "title": "tedair.gif",
                "mimetype": "image/gif",
                "filetype": "gif",
                "pretty_type": "GIF",
                "user": "U061F7AUR",
                "editable": false,
                "size": 137531,
                "mode": "hosted",
                "is_external": false,
                "external_type": "",
                "is_public": true,
                "public_url_shared": false,
                "display_as_bot": false,
                "username": "",
                "url_private": "https://.../tedair.gif",
                "url_private_download": "https://.../tedair.gif",
                "thumb_64": "https://.../tedair_64.png",
                "thumb_80": "https://.../tedair_80.png",
                "thumb_360": "https://.../tedair_360.png",
                "thumb_360_w": 176,
                "thumb_360_h": 226,
                "thumb_160": "https://.../tedair_=_160.png",
                "thumb_360_gif": "https://.../tedair_360.gif",
                "image_exif_rotation": 1,
                "original_w": 176,
                "original_h": 226,
                "deanimate_gif": "https://.../tedair_deanimate_gif.png",
                "pjpeg": "https://.../tedair_pjpeg.jpg",
                "permalink": "https://.../tedair.gif",
                "permalink_public": "https://.../...",
                "comments_count": 0,
                "is_starred": false,
                "shares": {
                    "public": {
                        "C0T8SE4AU": [
                            {
                                "reply_users": [
                                    "U061F7AUR"
                                ],
                                "reply_users_count": 1,
                                "reply_count": 1,
                                "ts": "1531763348.000001",
                                "thread_ts": "1531763273.000015",
                                "latest_reply": "1531763348.000001",
                                "channel_name": "file-under",
                                "team_id": "T061EG9R6"
                            }
                        ]
                    }
                },
                "channels": [
                    "C0T8SE4AU"
                ],
                "groups": [],
                "ims": [],
                "has_rich_preview": false
            },
            "comments": [],
            "response_metadata": {
                "next_cursor": "dGVhbTpDMUg5UkVTR0w="
            }
        }
        """

        payload = {"token": self._token, "file": file}

        if count is not None:
            payload["count"] = count

        if cursor is not None:
            payload["cursor"] = cursor

        if limit is not None:
            payload["limit"] = limit

        if page is not None:
            payload["page"] = page

        return self._get("files.info", payload=payload, **kwargs)

    def list(
        self,
        channel: str = None,
        count: int = None,
        page: int = None,
        show_files_hidden_by_limit: bool = None,
        ts_from: int = None,
        ts_to: int = None,
        types: str = None,
        user: str = None,
        **kwargs
    ) -> Response:
        """
        List for a team, in a channel, or from a user with applied filters.
        https://api.slack.com/methods/files.list

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channel: Filter files appearing in a specific channel, indicated by its ID.
        :type str: e.g. C1234567890

        :param count: Number of items to return per page.
        :type int: e.g. 20

        :param page: Page number of results to return.
        :type int: e.g. 2

        :param show_files_hidden_by_limit: Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit.
        :type bool: e.g. true

        :param ts_from: Filter files created after this timestamp (inclusive).
        :type int: e.g. 123456789

        :param ts_to: Filter files created before this timestamp (inclusive).
        :type int: e.g. 123456789

        :param types: Filter files by type (see below). You can pass multiple values in the types argument, like types=spaces,snippets.The default value is all, which does not filter the list.
        :type str: e.g. images

        :param user: Filter files created by a single user.
        :type str: e.g. W1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.list(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "files": [
                {
                    "id": "F0S43P1CZ",
                    "created": 1531763254,
                    "timestamp": 1531763254,
                    "name": "billair.gif",
                    "title": "billair.gif",
                    "mimetype": "image/gif",
                    "filetype": "gif",
                    "pretty_type": "GIF",
                    "user": "U061F7AUR",
                    "editable": false,
                    "size": 144538,
                    "mode": "hosted",
                    "is_external": false,
                    "external_type": "",
                    "is_public": true,
                    "public_url_shared": false,
                    "display_as_bot": false,
                    "username": "",
                    "url_private": "https://.../billair.gif",
                    "url_private_download": "https://.../billair.gif",
                    "thumb_64": "https://.../billair_64.png",
                    "thumb_80": "https://.../billair_80.png",
                    "thumb_360": "https://.../billair_360.png",
                    "thumb_360_w": 176,
                    "thumb_360_h": 226,
                    "thumb_160": "https://.../billair_=_160.png",
                    "thumb_360_gif": "https://.../billair_360.gif",
                    "image_exif_rotation": 1,
                    "original_w": 176,
                    "original_h": 226,
                    "deanimate_gif": "https://.../billair_deanimate_gif.png",
                    "pjpeg": "https://.../billair_pjpeg.jpg",
                    "permalink": "https://.../billair.gif",
                    "permalink_public": "https://.../...",
                    "channels": [
                        "C0T8SE4AU"
                    ],
                    "groups": [],
                    "ims": [],
                    "comments_count": 0
                },
                {
                    "id": "F0S43PZDF",
                    "created": 1531763342,
                    "timestamp": 1531763342,
                    "name": "tedair.gif",
                    "title": "tedair.gif",
                    "mimetype": "image/gif",
                    "filetype": "gif",
                    "pretty_type": "GIF",
                    "user": "U061F7AUR",
                    "editable": false,
                    "size": 137531,
                    "mode": "hosted",
                    "is_external": false,
                    "external_type": "",
                    "is_public": true,
                    "public_url_shared": false,
                    "display_as_bot": false,
                    "username": "",
                    "url_private": "https://.../tedair.gif",
                    "url_private_download": "https://.../tedair.gif",
                    "thumb_64": "https://.../tedair_64.png",
                    "thumb_80": "https://.../tedair_80.png",
                    "thumb_360": "https://.../tedair_360.png",
                    "thumb_360_w": 176,
                    "thumb_360_h": 226,
                    "thumb_160": "https://.../tedair_=_160.png",
                    "thumb_360_gif": "https://.../tedair_360.gif",
                    "image_exif_rotation": 1,
                    "original_w": 176,
                    "original_h": 226,
                    "deanimate_gif": "https://.../tedair_deanimate_gif.png",
                    "pjpeg": "https://.../tedair_pjpeg.jpg",
                    "permalink": "https://.../tedair.gif",
                    "permalink_public": "https://.../...",
                    "channels": [
                        "C0T8SE4AU"
                    ],
                    "groups": [],
                    "ims": [],
                    "comments_count": 0
                }
            ],
            "paging": {
                "count": 100,
                "total": 2,
                "page": 1,
                "pages": 1
            }
        }
        """

        payload = {"token": self._token}

        if channel is not None:
            payload["channel"] = channel

        if count is not None:
            payload["count"] = count

        if page is not None:
            payload["page"] = page

        if show_files_hidden_by_limit is not None:
            payload["show_files_hidden_by_limit"] = show_files_hidden_by_limit

        if ts_from is not None:
            payload["ts_from"] = ts_from

        if ts_to is not None:
            payload["ts_to"] = ts_to

        if types is not None:
            payload["types"] = types

        if user is not None:
            payload["user"] = user

        return self._get("files.list", payload=payload, **kwargs)

    def revoke_public_url(self, file: str, **kwargs) -> Response:
        """
        Revokes public/external sharing access for a file
        https://api.slack.com/methods/files.revokePublicURL

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param file: File to revoke
        :type str: e.g. F1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.revoke_public_url(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "file": file}

        return self._post("files.revokePublicURL", payload=payload, **kwargs)

    def shared_public_url(self, file: str, **kwargs) -> Response:
        """
        Enables a file for public/external sharing.
        https://api.slack.com/methods/files.sharedPublicURL

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param file: File to share
        :type str: e.g. F1234567890

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.shared_public_url(**your_params)
        <Response [200]>
        """

        payload = {"token": self._token, "file": file}

        return self._post("files.sharedPublicURL", payload=payload, **kwargs)

    def upload(
        self,
        channels: str = None,
        content: Union[str, IO] = None,
        file: Union[str, IO] = None,
        filename: str = None,
        filetype: str = None,
        initial_comment: str = None,
        thread_ts: float = None,
        title: str = None,
        **kwargs
    ) -> Response:
        """
        Uploads or creates a file.
        https://api.slack.com/methods/files.upload

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param channels: Comma-separated list of channel names or IDs where the file will be shared.
        :type str: e.g. C1234567890,C2345678901,C3456789012

        :param content: File contents via a POST variable. If omitting this parameter, you must provide a file.
        :type Union[str, IO]: e.g. '/absolute/path/to/file' or actual IO file

        :param file: File contents via multipart/form-data. If omitting this parameter, you must submit content.
        :type Union[str, IO]: e.g. '/absolute/path/to/file' or actual IO file

        :param filename: Filename of file.
        :type str: e.g. foo.txt

        :param filetype: A file type identifier.
        :type str: e.g. php

        :param initial_comment: The message text introducing the file in specified channels.
        :type str: e.g. Best!

        :param thread_ts: Provide another message's ts value to upload this file as a reply. Never use a reply's ts value; use its parent instead.
        :type float: e.g. 1234567890.123456

        :param title: Title of file.
        :type str: e.g. My File

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.files.upload(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "file": {
                "id": "F0TD00400",
                "created": 1532293501,
                "timestamp": 1532293501,
                "name": "dramacat.gif",
                "title": "dramacat",
                "mimetype": "image/jpeg",
                "filetype": "gif",
                "pretty_type": "JPEG",
                "user": "U0L4B9NSU",
                "editable": false,
                "size": 43518,
                "mode": "hosted",
                "is_external": false,
                "external_type": "",
                "is_public": false,
                "public_url_shared": false,
                "display_as_bot": false,
                "username": "",
                "url_private": "https://.../dramacat.gif",
                "url_private_download": "https://.../dramacat.gif",
                "thumb_64": "https://.../dramacat_64.gif",
                "thumb_80": "https://.../dramacat_80.gif",
                "thumb_360": "https://.../dramacat_360.gif",
                "thumb_360_w": 360,
                "thumb_360_h": 250,
                "thumb_480": "https://.../dramacat_480.gif",
                "thumb_480_w": 480,
                "thumb_480_h": 334,
                "thumb_160": "https://.../dramacat_160.gif",
                "image_exif_rotation": 1,
                "original_w": 526,
                "original_h": 366,
                "permalink": "https://.../dramacat.gif",
                "permalink_public": "https://.../More-Path-Components",
                "comments_count": 0,
                "is_starred": false,
                "shares": {
                    "private": {
                        "D0L4B9P0Q": [
                            {
                                "reply_users": [],
                                "reply_users_count": 0,
                                "reply_count": 0,
                                "ts": "1532293503.000001"
                            }
                        ]
                    }
                },
                "channels": [],
                "groups": [],
                "ims": [
                    "D0L4B9P0Q"
                ],
                "has_rich_preview": false
            }
        }
        """

        payload = {"token": self._token}

        if channels is not None:
            payload["channels"] = channels

        if content is not None:
            file_to_upload = make_file(content)
            payload["content"] = file_to_upload

        if file is not None:
            file_to_upload = make_file(file)
            kwargs["files"] = {"file": file_to_upload}

        if filename is not None:
            payload["filename"] = filename

        if filetype is not None:
            payload["filetype"] = filetype

        if initial_comment is not None:
            payload["initial_comment"] = initial_comment

        if thread_ts is not None:
            payload["thread_ts"] = thread_ts

        if title is not None:
            payload["title"] = title

        return self._post("files.upload", payload=payload, **kwargs)
