""" Запускаем модуль как самостоятельную программу
Для выполнения функции main() при запуске модуля как программы необходимо поместить её после проверки атрибута __name__.
Для тех, кто уже знаком с основами языка: далее в примерах вместо блоков в фигурных скобках подставляйте
переменные соответствующих типов данных. """


def main():
    pass


if __name__ == '__main__':
    main()
""" Разумеется, эта строчка не выполняется при обычном импорте модуля из другого файла. """