# -*- coding: utf-8 -*-
from requests import Response

from slack_time.api import SlackAPI


class Views(SlackAPI):
    def open(self, trigger_id: str, view: str, **kwargs) -> Response:
        """
        Open a view for a user.
        https://api.slack.com/methods/views.open

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param trigger_id: Exchange a trigger to post to the user.
        :type str: e.g. 12345.98765.abcd2358fdea

        :param view: A view payload. This must be a JSON-encoded string.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.views.open(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "view": {
                "id": "VMHU10V25",
                "team_id": "T8N4K1JN",
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "Quite a plain modal"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Create"
                },
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "a_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "A simple label",
                            "emoji": true
                        },
                        "optional": false,
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "an_action_id"
                        }
                    }
                ],
                "private_metadata": "Shh it is a secret",
                "callback_id": "identify_your_modals",
                "external_id": "",
                "state": {
                    "values": []
                },
                "hash": "156772938.1827394",
                "clear_on_close": false,
                "notify_on_close": false,
                "root_view_id": "VMHU10V25",
                "app_id": "AA4928AQ",
                "bot_id": "BA13894H"
            }
        }
        """

        payload = {"token": self._token, "trigger_id": trigger_id, "view": view}

        return self._post("views.open", payload=payload, **kwargs)

    def publish(
        self, user_id: str, view: str, hash: float = None, **kwargs
    ) -> Response:
        """
        Publish a static view for a User.
        https://api.slack.com/methods/views.publish

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param user_id: id of the user you want publish a view to.
        :type str: e.g. U0BPQUNTA

        :param view: A view payload. This must be a JSON-encoded string.
        :type str:

        :param hash: A string that represents view state to protect against possible race conditions.
        :type float: e.g. 156772938.1827394

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.views.publish(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "view": {
                "id": "VMHU10V25",
                "team_id": "T8N4K1JN",
                "type": "home",
                "close": null,
                "submit": null,
                "blocks": [
                    {
                        "type": "section",
                        "block_id": "2WGp9",
                        "text": {
                            "type": "mrkdwn",
                            "text": "A simple section with some sample sentence.",
                            "verbatim": false
                        }
                    }
                ],
                "private_metadata": "Shh it is a secret",
                "callback_id": "identify_your_home_tab",
                "state": {
                    "values": []
                },
                "hash": "156772938.1827394",
                "clear_on_close": false,
                "notify_on_close": false,
                "root_view_id": "VMHU10V25",
                "previous_view_id": null,
                "app_id": "AA4928AQ",
                "external_id": "",
                "bot_id": "BA13894H"
            }
        }
        """

        payload = {"token": self._token, "user_id": user_id, "view": view}

        if hash is not None:
            payload["hash"] = hash

        return self._post("views.publish", payload=payload, **kwargs)

    def push(self, trigger_id: str, view: str, **kwargs) -> Response:
        """
        Push a view onto the stack of a root view.
        https://api.slack.com/methods/views.push

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param trigger_id: Exchange a trigger to post to the user.
        :type str: e.g. 12345.98765.abcd2358fdea

        :param view: A view payload. This must be a JSON-encoded string.
        :type str:

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.views.push(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "view": {
                "id": "VNM522E2U",
                "team_id": "T9M4RL1JM",
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "Pushed Modal",
                    "emoji": true
                },
                "close": {
                    "type": "plain_text",
                    "text": "Back",
                    "emoji": true
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Save",
                    "emoji": true
                },
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "edit_details",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "detail_input"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Edit details"
                        }
                    }
                ],
                "private_metadata": "",
                "callback_id": "view_4",
                "external_id": "",
                "state": {
                    "values": []
                },
                "hash": "1569362015.55b5e41b",
                "clear_on_close": true,
                "notify_on_close": false,
                "root_view_id": "VNN729E3U",
                "previous_view_id": null,
                "app_id": "AAD3351BQ",
                "bot_id": "BADF7A34H"
            }
        }
        """

        payload = {"token": self._token, "trigger_id": trigger_id, "view": view}

        return self._post("views.push", payload=payload, **kwargs)

    def update(
        self,
        view: str,
        external_id: str = None,
        hash: float = None,
        view_id: str = None,
        **kwargs
    ) -> Response:
        """
        Update an existing view.
        https://api.slack.com/methods/views.update

        :param token: Authentication token bearing required scopes.
        :type str: e.g. xxxx-xxxxxxxxx-xxxx

        :param view: A view object. This must be a JSON-encoded string.
        :type str:

        :param external_id: A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either view_id or external_id is required.
        :type str: e.g. bmarley_view2

        :param hash: A string that represents view state to protect against possible race conditions.
        :type float: e.g. 156772938.1827394

        :param view_id: A unique identifier of the view to be updated. Either view_id or external_id is required.
        :type str: e.g. VMM512F2U

        :returns response:
        :type requests.Response: e.g. <Response [200]>

        example:
        >>> client = SlackTime(token='insert-your-token-here')
        >>> response = client.views.update(**your_params)
        <Response [200]>
        >>> response.json()
        {
            "ok": true,
            "view": {
                "id": "VNM522E2U",
                "team_id": "T9M4RL1JM",
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "Updated Modal",
                    "emoji": true
                },
                "close": {
                    "type": "plain_text",
                    "text": "Close",
                    "emoji": true
                },
                "submit": null,
                "blocks": [
                    {
                        "type": "section",
                        "block_id": "s_block",
                        "text": {
                            "type": "plain_text",
                            "text": "I am but an updated modal",
                            "emoji": true
                        },
                        "accessory": {
                            "type": "button",
                            "action_id": "button_4",
                            "text": {
                                "type": "plain_text",
                                "text": "Click me"
                            }
                        }
                    }
                ],
                "private_metadata": "",
                "callback_id": "view_2",
                "external_id": "",
                "state": {
                    "values": []
                },
                "hash": "1569262015.55b5e41b",
                "clear_on_close": true,
                "notify_on_close": false,
                "root_view_id": "VNN729E3U",
                "previous_view_id": null,
                "app_id": "AAD3351BQ",
                "bot_id": "BADF7A34H"
            }
        }
        """

        payload = {"token": self._token, "view": view}

        if external_id is not None:
            payload["external_id"] = external_id

        if hash is not None:
            payload["hash"] = hash

        if view_id is not None:
            payload["view_id"] = view_id

        return self._post("views.update", payload=payload, **kwargs)
