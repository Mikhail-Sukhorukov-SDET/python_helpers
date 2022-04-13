import random

YES_LIST = ('да', 'хочу', 'конечно', 'yes', 'of course', 'true', 'yeah', 'if', 'da', '+')
STOP_LIST = ('please, stop', 'stop', 'стоп', 'пожалуйста, остановите это')
BOTTOM_BOUND = 0


def set_upper_bound():
    while True:
        bound = input('Задайте верхнюю границу загаданному числу - ')
        if bound.isdigit():
            return int(bound)
        else:
            print(f'Введите пожалуйста число больше {BOTTOM_BOUND}.')


def prepare_hidden_number(bound):
    return random.randint(BOTTOM_BOUND, bound)


def is_valid(value, bound):
    if not value.isdigit():
        return False
    return BOTTOM_BOUND <= int(value) <= bound


print('Добро пожаловать в числовую угадайку!\nВведите "стоп" если хотите прервать игру')

upper_bound = set_upper_bound()
hidden_number = prepare_hidden_number(upper_bound)
counter, stop_counter = 0, 0

while True:
    number = input(f'Введите число от {BOTTOM_BOUND} до {upper_bound}: ')
    counter += 1
    if not is_valid(number, upper_bound):
        if number in STOP_LIST:
            stop_counter += 1
            if stop_counter < 4:
                print('Не отчаивайтесь - у вас все получится!')
            else:
                answer = input('Вы уверены что хотите прервать игру? ')
                if answer in YES_LIST:
                    break
        print(f'А может быть все-таки введем целое число от {BOTTOM_BOUND} до {upper_bound}?')
        continue
    else:
        number = int(number)
    if number < hidden_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif number > hidden_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print(f'Вы угадали, поздравляем!\nКоличевство попыток: {counter}')
        again = input('Хотите сыграть еще раз? - ').lower()
        if again in YES_LIST:
            upper_bound = set_upper_bound()
            hidden_number = prepare_hidden_number(upper_bound)
            counter, stop_counter = 0, 0
        else:
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
