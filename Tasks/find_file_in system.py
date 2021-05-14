import os


def obxodFile(path, file_name, level=1):
    #print('Папка', path)
    #print('level = ', level, 'Content:', os.listdir(path))
    for name in os.listdir(path):
        sub_path = os.path.join(path, name)
        if name == file_name:
            print(f"File '{file_name}' was found in {sub_path}")
            break
        elif os.path.isdir(sub_path):
            #print('Спускаемся в папку: ', sub_path)
            obxodFile(sub_path, file_name, level + 1)
            #print('Возвращаемся в папку: ', path)


path = "C:\\Riot Games"
file_name = "Aatrox.ru_RU.wad.client"

obxodFile(path, file_name)
