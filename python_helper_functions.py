print(type(()))
print(set("sdfasdf"))

a = {("asdf", "sdf"): "sdfsadfsadfasdf",
     4: 3,
     "sdfasdf": "Sdfsadfsf"}
b = a.keys()
print(b)


def min(first, *args):
    """ Dasha Jopa """
    res = first
    for arg in args:
        if arg < res:
            res = arg
    return res


xs = {-78, 154, 161}
print(min(*{-78, 154, 161}))
print(min.__doc__)


def bounded_min(first, *args, hi=float("inf"), lo=float("-inf")):
    """ To get min with bounds """
    res = hi
    for arg in (first,) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return max(res, lo)


print(bounded_min(*{-1000, 0, 546546}, hi=255, lo=0))


def unique(iterable, seen=set()):
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc


xs_list = [1, 1, 2, 3]
print(unique(xs_list))
print(unique(xs_list))


def unique_1(iterable, *, seen=None):
    seen = set(seen or [])
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc


xs_list = [1, 1, 2, 3]
print(unique_1(xs_list))
print(unique_1(xs_list))
set_ex = {2, 6, 5, 6, 5, 6, 5}
print(unique_1(xs_list, seen=set_ex))
print(unique_1(xs_list, seen=set_ex))


def runner(cmd, **kwargs):
    if kwargs.get("verbose", True):
        print("Bla bla bla")


runner("mysql", limit=42)
runner("mysql", verbose=123)
runner("ms", **{"verbose": False})
options = {"verbose": True}
runner("df", **options)


x = 1
y = 0
x, y = y, x
print(x, y)

first, *rest = range(5)
print(first, rest)

first, *rest, last = range(5)
print(first, rest, last)

*_, (first, *rest) = [range(1, 5)] * 5 + [range(456, 465)]
print(_)
print(first, rest)


def make_min(*, lo, hi):
    def inner(first, *args):
        res = hi
        for arg in (first, ) + args:
            if arg < res and lo < arg < hi:
                res = arg
        return max(res, lo)
    return inner


bounded_min_1 = make_min(lo=0, hi=255)
set_ex = {2, 6, 5, 6, 5, 6, 5}
print(bounded_min_1(*set_ex))



