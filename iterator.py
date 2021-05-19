""" Класс итератор """


class MyIterator:
    def __init__(self, collection):
        self.quantify = len(collection)
        self.iteration = 0
        self.collection = collection

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration < len(self.collection):
            self.iteration += 1
            return self.collection[self.iteration - 1]
        else:
            raise StopIteration("No more elements")


mi1 = MyIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(next(mi1))
# print(next(mi1))

for i in mi1:
    print(i)

# первый вариант
class Multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            pos, neg = 0, 0
            for func in self.funcs:
                if func(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(Multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)))
# [0, 30]

""" Второй вариант
class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iter(iterable)
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self


    def __next__(self):
        while True:
            element = next(self.iterable)
            pos, neg = 0, 0
            for func in self.funcs:
                if func(element):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                return element
"""