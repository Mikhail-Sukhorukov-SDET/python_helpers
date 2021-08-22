import random

print("Добро пожаловать в числовую угадайку")


while True:
    upper_bound = input('Задайте верхнюю границу загаданному числу - ')
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        break
    else:
        print('Давайте без глупостей - введите пожалуйста число.')

hidden_number = random.randint(0, upper_bound)
counter = 0


def is_valid(value):
    if not value.isdigit():
        return False
    return 0 <= int(value) <= upper_bound


while True:
    number = input(f'Введите число от 0 до {upper_bound}: ')
    counter += 1
    if not is_valid(number):
        print(f'А может быть все-таки введем целое число от 1 до {upper_bound}?')
        continue
    else:
        number = int(number)
    if number < hidden_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif number > hidden_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print(f'Количевство попыток: {counter}')
        again = input('Хотите сыграть еще раз? - ').lower()
        if again in ('да', 'хочу', 'конечно', 'yes', 'of course', 'true', 'yeah', 'if', 'da'):
            counter = 0
            hidden_number = random.randint(0, upper_bound)
            print('Число задано - приятной игры!')
        else:
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
