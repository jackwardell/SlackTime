# -*- coding: utf-8 -*-
from typing import IO
from typing import Union


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
        self.__doc__ = getattr(func, "__doc__")

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
            file_to_upload = f
    else:
        file_to_upload = file
    return file_to_upload
