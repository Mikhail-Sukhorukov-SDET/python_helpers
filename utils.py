from random import randint


def random_list(count_items=10, start=1, end=99):
    if not (isinstance(count_items, int) and isinstance(start, int) and isinstance(end, int)):
        raise TypeError(
            f"count_items not int but {type(count_items)}, start not int but {type(start)}, end not int but {type(end)}")
    return [randint(start, end) for _ in range(count_items)]


def get_max(nums_list: list) -> list:
    if not isinstance(nums_list, list):
        raise TypeError(f"nums_list not list but {type(nums_list)}")
    max_value = -1000000000
    for num in nums_list:
        if num >= max_value:
            max_value = num
    return max_value


def get_min(nums_list: list) -> list:
    if not isinstance(nums_list, list):
        raise TypeError(f"nums_list not list but {type(nums_list)}")
    min_value = 1000000000
    for num in nums_list:
        if num <= min_value:
            min_value = num
    return min_value


def zeros_count(number: int) -> int:
    """Return count of zero's from end of the number"""
    if not isinstance(number, list):
        raise TypeError(f"number not int but {type(number)}")
    last_number, counter = 0, 0
    while not last_number:
        last_number = number % 10
        number //= 10
        if not last_number:
            counter += 1
    return counter
