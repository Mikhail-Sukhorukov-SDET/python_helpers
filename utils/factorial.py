def factorial_recursive(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f"number not int but {type(number)}")
    if number == 1:
        return 1
    return factorial_recursive(number - 1) * number


def factorial_for(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f"number not int but {type(number)}")
    fct = 1
    for i in range(1, number + 1):
        fct *= i
    return fct


assert factorial_for(10) == factorial_recursive(10)
