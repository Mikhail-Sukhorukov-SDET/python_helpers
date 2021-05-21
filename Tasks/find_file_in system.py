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

list_of_dirs = set()
# через рекурсивный обход функцией TODO: доработать
"""
def look_for_a_file_by_end(path, end):
    for name in os.listdir(path):
        sub_path = os.path.join(path, name)
        if name.endswith(end):
            list_of_dirs.add(sub_path.replace(name, "").rstrip("\\").replace("\\", "/"))
        elif os.path.isdir(sub_path):
            look_for_a_file_by_end(sub_path, end)
    return list_of_dirs

os.chdir("C:\\Users\\hrumq\\PycharmProjects\\PythonHelpers\\Tasks\\Data")
with open("ans.txt", "w") as ans:
    [ans.write(f"{dir}\n") for dir in sorted(look_for_a_file_by_end("main", ".py"))]
"""

# через os.walk
os.chdir("C:\\Users\\hrumq\\PycharmProjects\\PythonHelpers\\Tasks\\Data")
[list_of_dirs.add(current_dir.replace("\\", "/")) for current_dir, dirs, files in os.walk("main") for file in files if file.endswith(".py")]
"""
for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            list_of_dirs.add(current_dir.replace("\\", "/"))
"""

with open("ans.txt", "w") as ans:
    [ans.write(f"{dir}\n") for dir in sorted(list_of_dirs)]
