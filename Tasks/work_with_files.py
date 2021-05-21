import json


def the_best_manager(file_name):
    with open(file_name, encoding='utf-8') as f:
        res = {}
        data = json.load(f)
        for i in range(len(data)):
            res[data[i]["manager"]["first_name"] + " " + data[i]["manager"]["last_name"]] = 0
            for car in data[i]["cars"]:
                res[data[i]["manager"]["first_name"] + " " + data[i]["manager"]["last_name"]] += car["price"]

        return sorted(res.items(), key=lambda value: value[1])[-1]


print(the_best_manager("Data/manager_sales.json"))


def group_people(file_name):
    with open(file_name, encoding='utf-8') as f:
        id = 0
        max_count = 0
        data = json.load(f)
        for i in range(len(data)):
            count = 0
            for people in data[i]["people"]:
                if people["gender"] == "Female" and people["year"] > 1977:
                    count += 1
            if count > max_count:
                max_count = count
                id = data[i]["id_group"]

        return id, max_count


print(group_people("Data/group_people.json"))


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


print(count_of_int("Data/numbers.txt"))


""" Revert file data """
with open("Data/dataset_24465_4.txt") as file:
    data = [line for line in file]
with open("Data/dataset_24465_4_reverted.txt", "w") as reverted:
    for line in data[::-1]:
        reverted.write(line)