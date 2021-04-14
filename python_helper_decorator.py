""" Should be finished """
import functools


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, func.__doc__, args, kwargs)
        return func(*args, **kwargs)

    return inner


@trace
def jopa_maker(something):
    """I return a jopa"""
    return print("jopa")


# help(jopa_maker)
list_ex = list(range(10))
jopa_maker(list_ex)
