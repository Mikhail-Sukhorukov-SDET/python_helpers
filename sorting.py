from utils import get_min


def bubble_sorting(random_list: list) -> list:
    if not isinstance(random_list, list):
        raise TypeError(f"random_list not list but {type(random_list)}")
    for i in range(len(random_list)):
        for j in range(len(random_list)):
            if random_list[i] <= random_list[j]:
                random_list[i], random_list[j] = random_list[j], random_list[i]
    return random_list


def select_sorting(random_list: list) -> list:
    if not isinstance(random_list, list):
        raise TypeError(f"random_list not list but {type(random_list)}")
    min_values = []
    for i in range(len(random_list)):
        slice_list = random_list[i:]
        min_value = slice_list.pop(slice_list.index(get_min(slice_list)))
        min_values.append(min_value)
        random_list = min_values + slice_list
    return random_list
