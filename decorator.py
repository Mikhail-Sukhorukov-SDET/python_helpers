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
def div(x, y):
    res = x / y
    return res


print(div(2, 4), "decorated @flip")
print(div.__wrapped__(2, 4), "__wrapped__ decorated @flip")


def introduce_on_debug(func):
    """
    Выводит имя функции если питон был вызван без флага -О:
    python -O decorator.py
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
print(example(9, introduce=False), "@optional_introduce\n\n")


def bucket(*decorator_args, **decorator_kwargs):
    def wrap(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print((decorator_args, decorator_kwargs))
            return func(*args, **kwargs)

        return inner

    return wrap


@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity1(x):
    return x


@bucket()
def identity2(x):
    return x


print(identity1(42))
print(identity2(42), "\n\n")


# maxsize - максимальный размер словаря
def memoized(maxsize=None):
    def inner(func):

        memory = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in memory:
                if len(memory) == maxsize:
                    memory.popitem()
                memory[key] = func(*args, **kwargs)
            return memory[key]

        return wrapper

    return inner


@memoized(maxsize=2)
def sum_of_two(a, b):
    print(a, b, end='; ')
    return a + b


print(sum_of_two(2, 0), '\n')
print(sum_of_two(2, 0), '\n')

print(sum_of_two(4, 2), '\n')
print(sum_of_two(4, 2), '\n')

print(sum_of_two(5, 0), '\n')
print(sum_of_two(5, 0), '\n')

print(sum_of_two(4, 2), '\n\n')


def decorator(new_decorator):
    def res_decorator(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            return new_decorator(func, *args, **kwargs)

        return new_func

    return res_decorator


@decorator
def introduce(f, *args, **kwargs):
    print(f.__name__)
    return f(*args, **kwargs)


@introduce
def identity4(x):
    return x


print(identity4(31415), "\n\n")

from functools import partial

con_class = partial(range, 0, 101)

for num in con_class(10):
    print(num)

print("\n\n")


from functools import wraps, partial


def bucket(func=None, **b_kwargs):
    if not func:
        return partial(bucket, **b_kwargs)

    @wraps(func)
    def inner(*args, **kwargs):
        print(b_kwargs)
        return func(*args, **kwargs)
    return inner


@bucket(two=2, three=3)
def identity(x):
    return x


print(identity(42))


def apply(*d_args, **d_kwargs):
    def inner(func):
        return func(*d_args, **d_kwargs)
    return inner


@apply(2, 3)
def multiply(x, y):
    return x * y


print(multiply, type(multiply))
