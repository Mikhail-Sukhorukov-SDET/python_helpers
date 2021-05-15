""" decorators """
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
    return print(f"jopa, {something}", end="\n\n")


help(jopa_maker)
list_ex = list(range(10))
jopa_maker(list_ex)


def flip(func):
    """ Задает позиционные аргументы функции в обратном порядке """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        args = sorted(args, reverse=True)
        return func(*args, **kwargs)

    return inner


@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res, end="\n\n")
    return res


div(2, 4, show=True)


def introduce_on_debug(func):
    """
    Выводит имя функции если питон был вызван без флага -О:
    python -O python_helper_decorator.py
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if __debug__:
            print(func.__name__)
        return func(*args, **kwargs)

    return inner


@introduce_on_debug
def identity(x):
    return x


print(identity(5), "@introduce_on_debug\n\n")


def optional_introduce(func):

    @functools.wraps(func)
    def inner(*args, introduce=False, **kwargs):
        if introduce:
            print(func.__name__)
        return func(*args, **kwargs)
    return inner


@optional_introduce
def example(x):
    return x


print(example(5), "@optional_introduce")
print(example(7, introduce=True), "@optional_introduce")
print(example(9, introduce=False), "@optional_introduce")
