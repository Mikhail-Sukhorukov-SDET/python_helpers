print(list(map(lambda x: x * 2, range(8))))  # map
print(list(filter(lambda x: x % 2 != 0, range(10))))  # filter
print(list(zip(["dsfs", "sdfsdfas", "asdfsadfs"], range(3))))  # zip
# генераторы списков, множевств и словарей
print([x * x for x in range(10) if x % 2 != 0])  # list
print({x * x for x in range(10) if x % 2 != 0})  # set
date = {"name": "Misha", "dreams": None, "money": "a little bit"}
print({k: v for k, v in date.items() if v})  # dict
