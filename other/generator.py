# с помощью генератора создаем итератор
def my_generator(collection):
    for i in collection:
        yield i


for i in my_generator(list(range(10))):
    print(i)