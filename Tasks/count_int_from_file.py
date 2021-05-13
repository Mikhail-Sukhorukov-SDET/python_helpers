"""
количество трехзначных чисел;
сумму двухзначных чисел
"""


def count_of_int(file_name):
    with open(file_name, encoding='utf-8') as f:
        l = list(map(int, f.read().split()))
        count_three = 0
        sum_two = 0
        for num in l:
            if 99 < num < 1000:
                count_three += 1
            if 9 < num < 100:
                sum_two += num

        return count_three, sum_two


print(count_of_int("numbers.txt"))
