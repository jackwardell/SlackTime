# -*- coding: utf-8 -*-
from unittest.mock import patch

import pytest
from requests import Session


def test_slack_api():
    from slack_time import SlackAPI

    token = "token"
    session = Session()
    proxies = {"http": "10.10.10.10"}
    timeout = 60

    api = SlackAPI(token, session, proxies, timeout)
    assert api._token == token
    assert api._session == session
    assert api._proxies == proxies
    assert api._timeout == timeout

    assert api.params == {
        "token": token,
        "session": session,
        "proxies": proxies,
        "timeout": timeout,
    }

    path = "hello"
    assert api.make_url(path) == f"https://slack.com/api/{path}"


def test_slack_api_get_request():
    with patch("slack_time.api.SlackAPI._request") as request:
        from slack_time import SlackAPI

        api = SlackAPI("token")
        path = "hello"
        payload = {"hello": "world"}
        kwargs = {"x": "y"}

        api._get(path, payload=payload, **kwargs)
        url = api.make_url(path)
        request.assert_called_once_with("get", url, params=payload, **kwargs)


def test_slack_api_post_request():
    with patch("slack_time.api.SlackAPI._request") as request:
        from slack_time import SlackAPI

        api = SlackAPI("token")
        path = "hello"
        payload = {"hello": "world"}
        kwargs = {"x": "y"}

        api._post(path, payload=payload, **kwargs)
        url = api.make_url(path)
        request.assert_called_once_with("post", url, data=payload, **kwargs)


def test_slack_api_request_requests():
    with patch("requests.request") as request:
        rv = {"ok": False, "error": "silly"}
        request.return_value = type("rv", (), {"json": (lambda: rv)})
        from slack_time import SlackAPI
        from slack_time import SlackError

        proxies = {"http": "10.10.10.10"}
        timeout = 60

        api = SlackAPI("token", proxies=proxies, timeout=timeout)
        method = "get"
        path = "hello"
        url = api.make_url(path)
        payload = {"hello": "world"}
        kwargs = {"x": "y"}

        resp = api._request(method, url, params=payload, **kwargs)
        request.assert_called_once_with(
            "get",
            url,
            params=payload,
            proxies=proxies,
            timeout=timeout,
            **kwargs,
        )
        assert resp.body == rv
        assert resp.successful == rv["ok"]
        assert resp.error == rv["error"]

        with pytest.raises(SlackError):
            api._get(path, payload=payload, **kwargs)
