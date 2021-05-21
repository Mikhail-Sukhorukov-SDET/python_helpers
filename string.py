""" Strings """

some_string = "foo bar"
cursed_string = "]>>foo bar<<["
blanked_string = "\t   foo bar \r \n"
symbol_string = "foo,bar"
symbols_string = "foo,,,bar"
file_name_example = "jopa.dopa.govno.jpg"

print(some_string.capitalize())
print(some_string.title())
print(some_string.upper())
print(some_string.lower())
print(some_string.title().swapcase())

# позиционирование строки
print(some_string.rjust(16, "-"))
print(some_string.ljust(16, "-"))
print(some_string.center(16, "-"))

print(some_string.rjust(16))
print(some_string.ljust(16))
print(some_string.center(16))

""" Strip - удаляет некоторые символы """
print("Strip")
print(cursed_string.lstrip("]>"))
print(cursed_string.rstrip("<["))
print(cursed_string.strip("[]<>"))

print(blanked_string.strip())  # по дефолту удаляет пробелы

""" Split - разделяте строку, создавая список элементов, второй аргумент это количевство разбиений """
print("Split")
print(symbol_string.split(","))
print(symbols_string.split(","))

print(blanked_string.split())  # по дефолту делит по пробелам
# есть rsplit
print(file_name_example.rsplit(".", 1))

""" Partition - создает кортеж из трех элементов по разделителю """
print("Partition")
print(file_name_example.partition('.'))
print(file_name_example.rpartition('.'))

""" Join - соединяет строки? """
print("Join")
print(".".join(["bar", "baz", "bar"]))
print(".".join("bar"))
print(".".join(filter(None, ["", "bar"])))

""" startswith endwith """
print(some_string.startswith("foo"))
print(some_string.endswith("foo"))

abr = "abracadabra"
""" find """
print(abr.find("ra"))
print(abr.find("ra", 0, 3))
# "abracadabra".index("ra", 0, 3)  будет ошибка


""" replace """
print(abr.replace("ra", "**"))
print(abr.replace("ra", "**", 1))

""" translation """
translation_map = {ord("a"): "!", ord("r"): "^"}
print(abr.translate(translation_map))

""" Format """
print("{0}, {1}, why are you a gay? {1}, {1}".format("Hello", "Sally"))  # !s, !r, !a
kek = {"x": 1, "y": 10}
print("point x: {0[x]}, point y: {0[y]}".format(kek))

print("%s, %s, why are you a gay?" % ("Hello", "Misha"))
kek1 = {"x": 12, "y": 0}
print("point x: %(x)2d, point y: %(y)d" % kek1)

""" Count """
name = "Helen"
print("'e' in 'Helen'", name.lower().count("e"))
