# -*- coding: utf-8 -*-
import requests


class SlackAPI:
    url = "https://slack.com/api"

    def __init__(self, token):
        self.token = token

    @property
    def params(self):
        return {"token": self.token}

    def make_url(self, path):
        return self.url + path

    def _post(self, path, payload=None, **kwargs):
        url = self.make_url(path)
        return requests.post(url, data=payload, **kwargs)

    def _get(self, path, payload=None, **kwargs):
        url = self.make_url(path)
        return requests.get(url, params=payload, **kwargs)

    def __repr__(self):
        name = self.__class__.__name__
        return f"<{name}(url={self.url + '/' + name.lower()})>"


class Endpoint:
    def __init__(self, url):
        self.url = url

    def get(self, params=None, **kwargs):
        return requests.get(self.url, params=params, **kwargs)

    def post(self, data=None, json=None, **kwargs):
        return requests.post(self.url, data=data, json=json, **kwargs)

    def request(self, method, **kwargs):
        return requests.request(method, self.url, **kwargs)

    def __call__(self, method, **kwargs):
        return self.request(method, **kwargs)
