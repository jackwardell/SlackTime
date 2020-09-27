# -*- coding: utf-8 -*-
import json
from collections.abc import Iterable
from functools import wraps
from typing import IO
from typing import Union


class SlackError(Exception):
    pass


class CachedProperty:
    """
    A property that is only computed once per instance and then replaces
    itself with an ordinary attribute. Deleting the attribute resets the
    property.

    Ripped from:
    https://github.com/python/cpython/blob/master/Lib/functools.py
    https://github.com/bottlepy/bottle/blob/master/bottle.py
    https://github.com/pydanny/cached-property/blob/master/cached_property.py
    """

    def __init__(self, func):
        self.func = func
        self.__doc__ = func.__doc__

    def __get__(self, instance, cls):
        if instance is None:
            return self
        value = instance.__dict__[self.func.__name__] = self.func(instance)
        return value


cached_property = CachedProperty


def make_file(file: Union[str, IO]):
    """
    for multipart/form-data

    for docstrings: e.g. '/absolute/path/to/file' or actual IO file"

    snippet:
    file_to_upload = make_file(file)
    payload["xxx"] = file_to_upload
    or
    kwargs["files"] = {"file": file_to_upload}
    """
    if isinstance(file, str):
        with open(file, "rb") as f:
            return f
    else:
        return file


def make_json_encoded(param: Union[str, list, dict]):
    if isinstance(param, str):
        return param
    elif isinstance(param, (list, dict)):
        return json.dumps(param)
    else:
        raise ValueError(
            "A JSON-encoded object must be passed to the function as either a "
            "string (JSON encoded) or a list or dict, which will be be "
            "converted by json.dumps to a JSON encoded string"
        )


def comma_separated_string(param: Union[str, Iterable]):
    if isinstance(param, str):
        return param
    elif isinstance(param, Iterable):
        return ",".join(param)
    else:
        raise ValueError(
            "A comma separated string must be passed as the comma separated "
            "string itself or as an iterable which will be joined with a comma"
        )


def raise_exception_on_error_from_server(func):
    @wraps(func)
    def wrapper(instance, path, **kwargs):
        resp = func(instance, path, **kwargs)
        if not resp.successful:
            url = SLACK_API_BASE_URL + "/" + path
            doc = SLACK_DOC_BASE_URL + url.rsplit("/", maxsplit=1).pop()
            exception = type(resp.error, (SlackError,), {})
            raise exception(
                f"You tried to perform a request to {url} \n"
                f"The server returned a '{resp.error}' response "
                f"Find out more at: {doc}#errors"
            )
        else:
            return resp

    return wrapper


SLACK_API_BASE_URL = "https://slack.com/api"
SLACK_DOC_BASE_URL = "https://api.slack.com/methods/"
