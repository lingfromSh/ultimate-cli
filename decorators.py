# DECORATORS.py
#   by Stephen Ling
#
# Created:
#   2020/1/24 下午2:41:58
# Last edited:
#   2020/1/24 下午4:58:15
# Auto updated?
#   Yes
#
# Description:
#   <Todo>
#

import typing as ty


def need_type(params: ty.Tuple = (), t: object = int, *args, **kwargs):
    """validate params."""
    if not isinstance(params, tuple):
        raise TypeError(f"param:params needs tuple, but got {type(params)}")
    if not isinstance(type, object):
        raise TypeError(f"param:type needs object, but got {type(type)}")

    def inner(func):
        def _inner(*args, **kwargs):
            for param in params:
                if not isinstance(r_param:=kwargs.get(param, None), t):
                    raise TypeError(
                        f"param:{param} need {t}, but got {type(r_param)}")
            return func(*args, **kwargs)
        return _inner
    return inner


@need_type(params=('params', 'supported'), t=tuple)
def only_supported_string(params: ty.Tuple, supported: ty.Tuple, *args, **kwargs):
    """ensure params' value must in supported."""
    def inner(func):
        def _inner(*args, **kwargs):
            for param in params:
                if (r_param:=kwargs.get(param, None)) not in supported:
                    raise ValueError(
                        f"param:[{param}={r_param}] is not supported.")
            return func(*args, **kwargs)
        return _inner
    return inner


if __name__ == "__main__":
    @need_type(params=('x',), t=str)
    def test(x=1):
        return
    test(x='1')

    @only_supported_string(params=('x',), supported=('0', '2'))
    def test(x):
        return
    test(x='1')