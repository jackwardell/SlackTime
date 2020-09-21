# -*- coding: utf-8 -*-

from functools import wraps

import requests

SLACK_API_BASE_URL = "https://slack.com/api"


class SlackError(Exception):
    pass


def enhance_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resp = func(*args, **kwargs)
        # got these features from:
        # https://github.com/os/slacker/blob/master/slacker/__init__.py
        resp.body = resp.json()
        resp.successful = resp.body["ok"]
        resp.error = resp.body.get("error")
        return resp

    return wrapper


def raise_exception_on_failure(func):
    @wraps(func)
    def wrapper(instance, path, **kwargs):
        resp = func(instance, path, **kwargs)
        if not resp.successful:
            url = SLACK_API_BASE_URL + "/" + path
            doc = "https://api.slack.com/methods/" + url.rsplit("/", maxsplit=1).pop()
            exception = type(resp.error, (SlackError,), {})
            raise exception(
                f"You tried to perform a request to {url}. \n"
                f"The server returned a '{resp.error}' response. "
                f"Find out more at: {doc}#errors"
            )
        else:
            return resp

    return wrapper


class SlackAPI:
    url = SLACK_API_BASE_URL

    def __init__(
        self,
        token: str,
        session: requests.Session = None,
        proxies: dict = None,
        timeout: int = 10,
    ):
        self.token = token
        self.session = session
        self.proxies = proxies
        self.timeout = timeout

    @property
    def params(self):
        rv = {
            "token": self.token,
            "session": self.session,
            "proxies": self.proxies,
            "timeout": self.timeout,
        }
        return rv

    def make_url(self, path: str) -> str:
        return self.url + "/" + path

    @enhance_response
    def _request(self, method: str, url: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", self.timeout)
        kwargs.setdefault("proxies", self.proxies)
        client = self.session if self.session else requests
        return client.request(method, url, **kwargs)

    @raise_exception_on_failure
    def _post(self, path: str, payload: dict = None, **kwargs) -> requests.Response:
        url = self.make_url(path)
        kwargs.setdefault("data", payload)
        return self._request("post", url, **kwargs)

    @raise_exception_on_failure
    def _get(self, path: str, payload: dict = None, **kwargs) -> requests.Response:
        url = self.make_url(path)
        kwargs.setdefault("params", payload)
        return self._request("get", url, **kwargs)

    def __repr__(self):
        name = self.__class__.__name__
        return f"<{name}(url={self.url + '/' + name.lower()})>"


# class Endpoint:
#     def __init__(self, url):
#         self.url = url
#
#     def get(self, params=None, **kwargs):
#         return requests.get(self.url, params=params, **kwargs)
#
#     def post(self, data=None, json=None, **kwargs):
#         return requests.post(self.url, data=data, json=json, **kwargs)
#
#     def request(self, method, **kwargs):
#         return requests.request(method, self.url, **kwargs)
#
#     def __call__(self, method, **kwargs):
#         return self.request(method, **kwargs)
