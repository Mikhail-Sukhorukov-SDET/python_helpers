""" Работаем со словарями
Получаем ключи, значения и пары ключ-значение из словарей: """
import collections


dict_ex = {"name": ["Mikhail", "Daria", "Dmitri"],
           "age": [23, 22, 22],
           "job": ["QA Aut", "Scientist", "None"]}
keys = dict_ex.keys()
values = dict_ex.values()
items = dict_ex.items()
print("keys", keys)
print("values", values)
print("items", items)

"""  чтобы получить элемент по ключу: """
dict_ex = {"name": ["Mikhail", "Daria", "Dmitri"],
           "age": [23, 22, 22],
           "job": ["QA Aut", "Scientist", "None"]}
value = dict_ex.get("name", None)  # Возвращает default, если ключ не найден.
print("value by key", value)
value = dict_ex.setdefault("sex", ["male", "female", "male"])  # То же, только с добавлением значения в словарь.
print("added value", value)
print("extended dict", dict_ex)

""" Python позволяет создавать словари со значениями по умолчанию. """
""" collections.defaultdict ничем не отличается от обычного словаря за исключением того, 
что по умолчанию всегда вызывается функция, возвращающая значение: """
dict_default_type = collections_ex.defaultdict(list)  # Создаёт словарь с дефолтным значением type.
print("default dict idk", dict_default_type)
for i in range(5):
    dict_default_type[i].append(i)
print("default dict idk", dict_default_type)
dict_default_lambda_1 = collections_ex.defaultdict(lambda: 1)  # Создаёт словарь с дефолтным значением 1.
print("default dict idk", dict_default_lambda_1)

""" Также можно создавать словари из последовательностей пар ключ-значение или из двух последовательностей: """
collection_new = [("Mikhail", 23), ("Daria", 22), ("Mark", 25), ("John", 26), ("Andrew", 30)]
new_dict = dict(collection_new)
print("new dict by collection", new_dict)
new_dict = dict(zip(["name", "job", "age"], ["Mikhail", "QA Aut", 23]))
print("new dict by two arguments", new_dict)

""" Как и у Python списков, словари поддерживают операцию pop. Только удаление элемента происходит по ключу: """
value = new_dict.pop("age")
print("deleted value", value)
print("cut dict", new_dict)

""" Смотрите, как красиво можно отфильтровать словарь по ключу: """
collection_new = [("Mikhail", 23), ("Daria", 22), ("Mark", 25), ("John", 26), ("Andrew", 30)]
old_dict = dict(collection_new)
print(old_dict)
print(old_dict.keys())
old_dict_keys = ["Mikhail", "Daria"]
dict_i_want = {k: v for k, v in old_dict.items() if k in old_dict_keys}
print("filtration by dict", dict_i_want)

dict_ex = {1: 1,
           "b": 2}
dict_ac = {1: 1,
           "b": 2}
for i in dict_ex.keys():
    print(dict_ex[i], dict_ac[i])
    assert dict_ex[i] == dict_ac[i]


