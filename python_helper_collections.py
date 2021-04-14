""" Обработка коллекций """
from collections import namedtuple

personal_data = ("Mikhail", "Sukhorukov", "November", 10, 1996)
name, birthday = personal_data[:2], personal_data[2:]
print(name)
print(birthday)
NAME, BIRTHDAY = slice(2), slice(2, None)
print(personal_data[NAME])
print(personal_data[BIRTHDAY])

Person = namedtuple("Person", ["name", "age"])
p = Person("Mikhail", age=23)
print(p._fields, p.name, p.age)
print(p._asdict())
print(p._replace(name="Jopa"))

print([0] * 2)
print([""] * 2)
a = [[0]] * 2
print(a)
a[0][0] = 42
print(a)
list_gen = [[0] for i in range(5)]
print(list_gen)
list_gen[2][0] = 55
print(list_gen)
list_ex = [1, 2, 3]
list_ex.append(5)
print(list_ex)
list_ex.extend([6, 8, 9])
print(list_ex)
list_ex.insert(0, "sdfaf")
print(list_ex)
list_ex.insert(-1, "jopa")
print(list_ex)
list_ex[:2] = [0] * 2
print(list_ex)
print(list(reversed(list_ex)))
xs = [9, 5, 2]
xs.sort()
print(xs)
xs = [9, 5, 2]
print(sorted(xs))
xs.sort(key=lambda x: x % 2, reverse=True)
print(xs)
