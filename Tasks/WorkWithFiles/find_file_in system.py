import os


def look_for_a_file_by_full_name(path, file_name, level=1):
    # print('Папка', path)
    # print('level = ', level, 'Content:', os.listdir(path))
    for name in os.listdir(path):
        sub_path = os.path.join(path, name)
        if name == file_name:
            print(f"File '{file_name}' was found in {sub_path}")
            break
        elif os.path.isdir(sub_path):
            # print('Спускаемся в папку: ', sub_path)
            look_for_a_file_by_full_name(sub_path, file_name, level + 1)
            # print('Возвращаемся в папку: ', path)


path = "C:\\Riot Games"
file_name = "Aatrox.ru_RU.wad.client"

look_for_a_file_by_full_name(path, file_name)

""" All dirs with files that end with ".py" """


# через рекурсивный обход функцией TODO: доработать

def look_for_a_file_by_end(path, end, dirs=None):
    if dirs == None:
        dirs = set()
    for name in os.listdir(path):
        sub_path = os.path.join(path, name)
        if name.endswith(end):
            dirs.add(sub_path.replace(name, "").rstrip("\\").replace("\\", "/"))
        if os.path.isdir(sub_path):
            look_for_a_file_by_end(sub_path, end, dirs)
    return dirs


os.chdir("\\Tasks\\WorkWithFiles\\Data")
with open("ans.txt", "w") as ans:
    [ans.write(f"{dir}\n") for dir in sorted(look_for_a_file_by_end("main", ".py"))]

# через os.walk
dirs_with_py = set()
os.chdir("\\Tasks\\WorkWithFiles\\Data")
[dirs_with_py.add(current_dir.replace("\\", "/")) for current_dir, dirs, files in os.walk("main") for file in files if
 file.endswith(".py")]

for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            dirs_with_py.add(current_dir.replace("\\", "/"))

with open("ans.txt", "w") as ans:
    [ans.write(f"{dir}\n") for dir in sorted(dirs_with_py)]
