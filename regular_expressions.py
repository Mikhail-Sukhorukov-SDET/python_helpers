import re

"""
https://docs.python.org/3.5/library/re.html
print(re.match)
print(re.search)
print(re.findall)
print(re.sub)

. ^ $ * + ? { } [ ] \ | ( ) — метасимволы
[ ] — можно указать множество подходящих символов
^ - карет, обозначает либо начало строки, либо инвертирование группы символов. (например: "^[^0-9]" — не-цифра в начале строки).
/d - [0-9] — цифры
/D - [^0-9]
/s - [ \t\n\r\f\v] — пробельные символы
/S - [^ \t\n\r\f\v]
/w - [a-zA-Z0-9_] — буквы + цифры + _
/W - [^a-zA-Z0-9_]
/b - Matches the empty string, but only at the beginning or end of a word.
This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
/B - Matches the empty string, but not at the beginning or end of a word.
This means that r'py\B' matches 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'.
ab*aaa - звезда показывает что мы ищем любое колличевство символов b 
"""

pattern = r"a[abcd]c"
string = "abc"
inv_string = "ajc"
# проверка попадает ли под паттерн
print(re.match(pattern, string))
print(re.match(pattern, inv_string), end="\n")

# поиск попадающего под паттерн
strings = "abc, ajc, m, abb, aac"
all_inclusions = re.findall(pattern, strings)
print(all_inclusions, end="\n")

# замена попадающего под паттерн на abc
fixed = re.sub(pattern, "abc", strings)
print(fixed, end="\n")

# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
strings = ["catcat", "cat and cat", "catac", "cat", "ccaatt"]
for line in strings:
    line = line.rstrip()
    if re.search(r"cat.*cat", line):
        print(line)
print()

# Выведите строки, содержащие "cat" в качестве слова.
strings = ["cat", "catapult and cat", "catcat", "concat", "Cat", "'cat'", "!cat?"]
for line in strings:
    line = line.rstrip()
    if re.search(r"\bcat\b", line):
        print(line)
print()

# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
strings = ["zabcz", "zzz", "zzxzz", "zz", "zxz", "zzxzxxz"]
for line in strings:
    line = line.rstrip()
    if re.search(r"z.{3}z", line):
        print(line)
print()

# Выведите строки, содержащие обратный слеш "\".
strings = ["\w denotes word character", "No slashes here"]
for line in strings:
    line = line.rstrip()
    if re.search(r"\\", line):
        print(line)
print()

# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
strings = ["blabla is a tandem repetition", "123123 is good too", "go go", "aaa"]
for line in strings:
    line = line.rstrip()
    if re.search(r"\b(\w+)\1\b", line):
        print(line)
print()

# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
strings = ["I need to understand the human mind", "humanity"]
for line in strings:
    line = line.rstrip()
    print(re.sub("human", "computer", line))
print()

# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен),
# на слово "argh".
strings = ['There’ll be no more "Aaaaaaaaaaaaaaa"', 'AaAaAaA AaAaAaA']
for line in strings:
    line = line.rstrip()
    print(re.sub(r"\b[a|A]+\b", "argh", line, count=1))
print()

# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
strings = ["this is a text", '"this\' !is. ?n1ce,']
for line in strings:
    line = line.rstrip()
    print(re.sub(r"\b(\w{0}\w{1})(\w{1}\w{0})", r"\2\1", line))
print()


# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
strings = ["attraction", "buzzzz"]
for line in strings:
    line = line.rstrip()
    print(re.sub(r"(\w{1})\1+", r"\1", line))
print()
