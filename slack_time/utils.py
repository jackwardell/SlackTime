# -*- coding: utf-8 -*-
from functools import update_wrapper, wraps


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
