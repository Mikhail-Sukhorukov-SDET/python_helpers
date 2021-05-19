print(list(map(lambda x: x * 2, range(8))))  # map
print(list(filter(lambda x: x % 2 != 0, range(10))))  # filter
print(list(zip(["dsfs", "sdfsdfas", "asdfsadfs"], range(3))))  # zip

# генераторы списков, множевств и словарей
print([x * x for x in range(10) if x % 2 != 0])  # list
print({x * x for x in range(10) if x % 2 != 0})  # set
date = {"name": "Misha", "dreams": None, "money": "a little bit"}
print({k: v for k, v in date.items() if v})  # dict

d = {'Джек': 2.5, 'Билл': 4.0}
# сортировака в первую очерердь от большего к меньшему по значениям и во вторую по алфавиту по ключам
for item in sorted(d.items(), key= lambda kv: (-kv[1], kv[0])):
    print(item[0], item[1])

# выражение генератор - можно обойти только один раз
a = (i for i in range(4, 21) if i % 5 == 0)
for i in a:
    print(i)

# экономит память - элементы не хранятся в памяти - в списке такое не сохранить
c = (i for i in range(10000000000))
