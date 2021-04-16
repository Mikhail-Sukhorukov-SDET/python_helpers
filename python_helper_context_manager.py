""" Context Managers """

"How it looks"
with open('some_file.txt', 'w') as opened_file:
    opened_file.write('Hola!')

"Under the hood"
opened_file = open('some_file.txt', 'w')
try:
    opened_file.write('Hola!')
finally:
    opened_file.close()

"As class"


class File(object):
    def __init__(self, file_name, method):
        print("init")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("enter")
        return self.file_obj

    def __exit__(self, type, value, traceback):
        """ As I understand 'type' is type of Error """
        print("exit")
        self.file_obj.close()
        if type is AttributeError:  # here handled AttributeError cause File class doesn't have a "wriite" attribute
            return True


with File('some_file.txt', 'w') as opened_file:
    opened_file.wriite('Hello!')
