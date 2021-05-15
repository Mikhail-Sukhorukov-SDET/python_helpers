min  # builtin

min = 43  # global

print(globals())


def f():
    min = 2  # enclosing

    # print(locals())
    def g():
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


# замыкание
def multiply(n1):
    def mul(n2):
        return n1 * n2

    return mul


f_2 = multiply(2)
print("Умножение 2 на 5 =", f_2(5))  # 10
print("Умножение 2 на 15 =", f_2(15))  # 30
f_3 = multiply(3)
print("Умножение 3 на 5 =", f_3(5))  # 15
print("Умножение 3 на 15 =", f_3(15))  # 45


def composition(f, g):
    def inner(*args):
        return f(g(*args))

    return inner


h = composition(lambda x: x ** 2, lambda x: x + 1)
print(h(5))

h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
print(h(5))

h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
print(h(2, 3, 9))