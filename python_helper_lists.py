import functools
import itertools
import collections

""" Приручаем Python списки
В языке Python удобно получать срез списка от элемента с индексом from_inclusive до to_exclusive с шагом step_size: """
listor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_edited = listor[3:8:2]
print("срез по индексу", list_edited)
list1 = ["a", "b", "c", "d", "e", "f"]
""" Посмотрите, как добавить элемент или коллекцию элементов в список: """
list1.append(6)
list1 += [6]
print("append", list1)
""" А вот так мы расширим список другим списком: """
listor.extend(list_edited)
listor += list_edited
print("extend", listor)
""" Перейдём к прямой и обратной сортировке. Кроме reverse() и reversed() для обратной сортировки можно также 
использовать sort() и sorted() с флагом reverse=True. """
list_sort = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list_sort.sort()
print("sort", list_sort)
list_sort.reverse()
print("reverse", list_sort)
print("sorted", sorted(list_sort))
list_reversed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("reversed", list(reversed(list_reversed)))
collection_to_be_sorted = [("Mikhail", 23, "QA Aut"), ("John", 40, "Dev"), ("Daria", 22, "Scientist")]
sorted_by_second = sorted(collection_to_be_sorted, key=lambda el: el[1])
print("sorted by 1 par", sorted_by_second)
sorted_by_both = sorted(collection_to_be_sorted, key=lambda el: (el[2], el[1]))
print("sorted by 2 par???????", sorted_by_both)
""" Суммируем элементы: """
list_to_sum1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list_to_sum2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
sum_of_elements = sum(list_to_sum1)
print("sum elements", sum_of_elements)
elementwise_sum = [sum(pair) for pair in zip(list_to_sum1, list_to_sum2)]
print("sum elements from 2 lists by index", elementwise_sum)
""" Преобразовываем несколько списков в один: """
collection_j = [(10, 23, 13), (11, 40, 14), (12, 22, 15)]
list_to_unitize = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
flatter_list = list(itertools.chain.from_iterable(collection_j))
print("from dict to list", flatter_list)
product_of_elems = functools.reduce(lambda out, x: out + x, list_to_unitize)
print("sum of elements", product_of_elems)
""" Получаем список символов из строки: """
string_example = "asdfdsfasfasfasf"
list_of_chars = list(string_example)
print("to list from string", list_of_chars)
""" Чтобы получить первый индекс элемента: """
index_list = list_of_chars.index("f")
print("get first index of element from list", index_list)
index_string = string_example.index("f")
print("get first index of element from string", index_string)
""" Делаем вставку и удаление по индексу: """
list_insert = [1, 2, 3, 4, 5]
list_insert.insert(1, "Sdfadsfasdfs")
print("replace of element by index", list_insert)
list_insert = [1, 2, 3, 4, 5]
el = list_insert.pop(4)  # удаляет элемент по индексу и возвращает его или последний элемент.
print("removed element", el)
print("list without removed element", list_insert)
list_insert = [1, 1, 3, 4, 5]
list_insert.remove(1)
print("remove first founded element", list_insert)  # удаляет элемент в первом обнаружении или выдаёт ошибку ValueError.
list_insert = [1, 1, 3, 4, 5]
list_insert.clear()  # Удаляет все элементы
print("clear", list_insert)

""" collections.Counter - вид словаря, который позволяет нам считать количество неизменяемых объектов 
(в большинстве случаев, строк). Пример: """
c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] += 1
print(c)
print(c['counter'])
print(c['collections'])
