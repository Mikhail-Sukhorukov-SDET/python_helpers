def fib(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fib(x-2) + fib(x -1)
print(fib(5))

def fiban(x):
    fib1 = 0
    fib2 = 1
    for i in range(2, x):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2
print(fiban(5))