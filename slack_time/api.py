# -*- coding: utf-8 -*-
import requests
from slack_time.utils import raise_exception_on_error_from_server
from slack_time.utils import SLACK_API_BASE_URL


class SlackAPI:
    """
    Base API for all Slack endpoints.

    :param token: slack api token
    :type str: e.g. xoxo-3243434543w5-XXXXXXX

    :param session: requests session object
    :type request.Session:

    :param proxies: http and https proxies
    :type dict: e.g. {"http": 10.10.10.10, "https": 10.11.12.13}

    :param timeout: number of seconds for timeout
    :type int: e.g. 60 (for 60s)
    """

    url = SLACK_API_BASE_URL

    def __init__(
        self,
        token: str,
        session: requests.Session = None,
        proxies: dict = None,
        timeout: int = 10,
    ):
        self._token = token
        self._session = session
        self._proxies = proxies
        self._timeout = timeout

    @property
    def params(self) -> dict:
        rv = {
            "token": self._token,
            "session": self._session,
            "proxies": self._proxies,
            "timeout": self._timeout,
        }
        return rv

    def make_url(self, path: str) -> str:
        return self.url + "/" + path

    def _request(self, method: str, url: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", self._timeout)
        kwargs.setdefault("proxies", self._proxies)
        client = self._session if self._session else requests

        resp = client.request(method, url, **kwargs)
        # got these features from:
        # https://github.com/os/slacker/blob/master/slacker/__init__.py
        resp.body = resp.json()
        resp.successful = resp.body["ok"]
        resp.error = resp.body.get("error")
        return resp

    @raise_exception_on_error_from_server
    def _post(
        self, path: str, payload: dict = None, **kwargs
    ) -> requests.Response:
        url = self.make_url(path)
        kwargs.setdefault("data", payload)
        return self._request("post", url, **kwargs)

    @raise_exception_on_error_from_server
    def _get(
        self, path: str, payload: dict = None, **kwargs
    ) -> requests.Response:
        url = self.make_url(path)
        kwargs.setdefault("params", payload)
        return self._request("get", url, **kwargs)
