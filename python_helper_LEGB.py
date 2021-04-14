min  # builtin

min = 43  # global


print(globals())
def f():
    min = 2

    # print(locals())
    def g():  # enclosing
        min = 0  # local
        print(min)


f()


def f():
    print(i)


for i in range(5):
    f()

min = 49


def f():
    global min
    min += 1
    return min


print(f())


def cell(value=None):
    def get():
        return value

    def set(update):
        nonlocal value
        value = update

    return get, set


get, set = cell()
set(42)
print(get())
