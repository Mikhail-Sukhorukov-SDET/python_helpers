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
            return self.collection[self.iteration-1]
        else:
            raise StopIteration("No more elements")


mi1 = MyIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(next(mi1))
# print(next(mi1))

for i in mi1:
    print(i)
