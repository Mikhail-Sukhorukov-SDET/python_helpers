""" Immutable """
print("Immutable")
a = (1, 2, 3)
b = a
b += (4, 5)
print(b, type(b))
print(a, type(a))

a = "str"
b = a
b += "str"
print(b, type(b))
print(a, type(a))

a = 1
b = a
b += 1
print(b, type(b))
print(a, type(a))

""" Mutable """
print("Mutable")
a = [1, 2, 3]
b = a
b += [4, 5]
print(b, type(b))
print(a, type(a))

a = {1, 2, 3}
b = a
b.add(4)
print(b, type(b))
print(a, type(a))

a = {"sex": "male", "name": "Misha", "jopa": "chicken"}
b = a
b["surname"] = "Sukhorukov"
print(b, type(b))
print(a, type(a))


