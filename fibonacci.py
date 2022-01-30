def fibonacci_recursive(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f"number not int but {type(number)}")
    if number == 1:
        return 0
    if number == 2:
        return 1
    return fibonacci_recursive(number - 2) + fibonacci_recursive(number - 1)


def fibonacci_for(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f"number not int but {type(number)}")
    fib1 = 0
    fib2 = 1
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


assert fibonacci_for(10) == fibonacci_recursive(10)
