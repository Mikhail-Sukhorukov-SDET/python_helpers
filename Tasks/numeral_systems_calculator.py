def break_a_number_into_digits(number):
    count, number_dict = 0, {}
    if isinstance(number, int):
        while number:
            number_dict[count] = number % 10
            count += 1
            number //= 10
    elif isinstance(number, str):
        for i in range(len(number)):
            number_dict[len(number) - i - 1] = int(number[i]) if number[i].isdigit() else number[i]
    else:
        raise ValueError
    return number_dict


def revert_to_decimal(numerical_system: int, number):
    if not isinstance(numerical_system, int) or not isinstance(number, (int, str)):
        raise ValueError
    split_number, result = break_a_number_into_digits(number), 0
    for key, value in split_number.items():
        if isinstance(value, str):
            value = ord(value) - 55
        result += value * numerical_system ** key
    return result


def revert_from_decimal(numerical_system: int, number: int):
    if not isinstance(numerical_system, int) or not isinstance(number, int):
        raise ValueError
    result = ""
    while True:
        modulo = str(number % numerical_system)
        if numerical_system > 10 and int(modulo) > 10:
            modulo = chr(int(modulo) + 55)
        result = modulo + result
        if number // numerical_system < numerical_system:
            result = str(number // numerical_system) + result
            return result
        else:
            number = (number - number % numerical_system) // numerical_system


""" https://stepik.org/lesson/349851/step/3?unit=333706 """
print(111111, 2, revert_to_decimal(2, 111111))

""" https://stepik.org/lesson/349851/step/4?unit=333706 """
print("1AF2", 16, revert_to_decimal(16, "1AF2"))

""" https://stepik.org/lesson/349851/step/5?unit=333706 """
for i in range(2, 16):
    if revert_to_decimal(i, 88) == revert_to_decimal(
            i, 32) + revert_to_decimal(i, 22) + revert_to_decimal(i, 16) + revert_to_decimal(i, 17):
        print(i)
        break

""" https://stepik.org/lesson/349851/step/7?unit=333706 """
print(revert_from_decimal(16, 1000))

""" https://stepik.org/lesson/349851/step/8?unit=333706 """
print(revert_from_decimal(2, 513))
