'''
Filename: /home/ling/文档/ultimate-cli/decorators.py
Path: /home/ling/文档/ultimate-cli
Created Date: Sunday, January 26th 2020, 2:24:40 pm
Author: ling

Copyright (c) 2020 Your Company
'''


import typing as ty


def need_type(params: ty.Tuple = (), t: object = int, *args, **kwargs):
    """validate params."""
    if not isinstance(params, tuple):
        raise TypeError(f"param:[params] needs tuple, but got {type(params)}")
    if not isinstance(type, object):
        raise TypeError(f"param:[type] needs object, but got {type(type)}")

    def inner(func):
        def _inner(*args, **kwargs):
            for param in params:
                if not isinstance(kwargs.get(param, None), t):
                    raise TypeError(
                        f"param:[{param}] need {t}, but got {type(kwargs.get(param, None))}")
            return func(*args, **kwargs)
        return _inner
    return inner


@need_type(params=('param',), t=str)
@need_type(params=('keys',), t=set)
def need_keys(param: ty.AnyStr, keys: ty.Set, *args, **kwargs):
    """ensure dict has needed key."""
    def inner(func):
        def _inner(*args, **kwargs):
            d = kwargs.get(param)
            if keys & d.keys() != keys:
                raise KeyError(f"Need keys:{keys ^ d.keys()}")
            return func(*args, **kwargs)
        return _inner
    return inner


@need_type(params=('params', 'supported'), t=tuple)
def only_supported_elements(params: ty.Tuple, supported: ty.Tuple, *args, **kwargs):
    """ensure params' value must in supported."""
    def inner(func):
        def _inner(*args, **kwargs):
            for param in params:
                if (kwargs.get(param, None)) not in supported:
                    raise ValueError(
                        f"[{param}={kwargs.get(param, None)}] is not supported.")
            return func(*args, **kwargs)
        return _inner
    return inner


if __name__ == "__main__":
    @only_supported_elements(params=('x',), supported=('0', '2'))
    @need_type(params=('x',), t=str)
    def test(x=1):
        return
    test(x='1')
