""" Should be finished """
import functools


def trace(func):
    # этот декоратор позволяет возвращать имя и документацию декорируемой функции
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


@trace
def jopa_maker(something):
    """I return a jopa"""
    return print(f"jopa, {something}")


help(jopa_maker)
list_ex = list(range(10))
jopa_maker(list_ex)
