""" Обработка коллекций """
from collections import namedtuple

personal_data = ("Mikhail", "Sukhorukov", "November", 10, 1996)
name, birthday = personal_data[:2], personal_data[2:]
print("name, birthday = personal_data[:2], personal_data[2:] -", name, birthday)
NAME, BIRTHDAY = slice(2), slice(2, None)
print("NAME, BIRTHDAY = slice(2), slice(2, None) -", personal_data[NAME], personal_data[BIRTHDAY])

Person = namedtuple("Person", ["name", "age"])
p = Person("Mikhail", age=23)
print("namedtuple('Person', ['name', 'age'])", "Person('Mikhail', age=23) -", p._fields, p.name, p.age)
print("namedtuple('Person', ['name', 'age'])", "Person('Mikhail', age=23) -", p._asdict())
print("namedtuple('Person', ['name', 'age'])", "Person('Mikhail', age=23) -", p._replace(name="Jopa"))

print("print([0] * 2) -", [0] * 2)

print("print([""] * 2) -", [""] * 2)

a = [[0]] * 2
print("print([[0]] * 2) -", [[0]] * 2)

a[0][0] = 42
print("print(a[0][0] = 42) -", a)

list_gen = [[0] for i in range(5)]
print("[[0] for i in range(5)] -", list_gen)

list_gen[2][0] = 55
print("[[0] for i in range(5)] list_gen[2][0] = 55 -", list_gen)

list_ex = [1, 2, 3]
list_ex.append(5)
print("list_ex = [1, 2, 3] list_ex.append(5) -", list_ex)

list_ex = [1, 2, 3]
list_ex.extend([6, 8, 9])
print("list_ex = [1, 2, 3] list_ex.extend([6, 8, 9]) -", list_ex)

list_ex = [1, 2, 3]
list_ex.insert(0, "sdfaf")
print("list_ex = [1, 2, 3] list_ex.insert(0, 'sdfaf') -", list_ex)

list_ex = [1, 2, 3]
list_ex.insert(-1, "jopa")
print("list_ex = [1, 2, 3] list_ex.insert(-1, 'jopa') -", list_ex)

list_ex = [1, 2, 3]
list_ex[:2] = [0] * 2
print("list_ex = [1, 2, 3] list_ex[:2] = [0] * 2 -", list_ex)

list_ex = [1, 2, 3]
print("list_ex = [1, 2, 3] list(reversed(list_ex)) -", list(reversed(list_ex)))

xs = [9, 5, 2]
xs.sort()
print("xs = [9, 5, 2] xs.sort() -", xs)

xs = [9, 5, 2]
print("xs = [9, 5, 2] sorted(xs) -", sorted(xs))

xs.sort(key=lambda x: x % 2, reverse=True)
print("xs = [2, 5, 9] xs.sort(key=lambda x: x % 2, reverse=True) -", xs)
