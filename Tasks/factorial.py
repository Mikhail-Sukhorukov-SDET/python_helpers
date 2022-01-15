def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(factorial(5))


def trailing_zeros(n: int) -> int:
    n = factorial(n)
    last_number, counter = 0, 0
    while last_number == 0:
        last_number = n % 10
        n //= 10
        if last_number == 0:
            counter += 1
    return counter


print(trailing_zeros(20))


def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


print(fact(4))
