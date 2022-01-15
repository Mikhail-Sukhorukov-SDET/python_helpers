def factorial_for(n):
    fct = 1
    for i in range(1, n + 1):
        fct *= i
    return fct


print(factorial_for(5))


def trailing_zeros(n: int) -> int:
    n = factorial_for(n)
    last_number, counter = 0, 0
    while not last_number:
        last_number = n % 10
        n //= 10
        if not last_number:
            counter += 1
    return counter


print(trailing_zeros(20))


def factorial_recursive(n):
    if n == 1:
        return 1
    return factorial_recursive(n - 1) * n


print(factorial_recursive(4))
