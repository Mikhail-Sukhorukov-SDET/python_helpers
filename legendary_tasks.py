""" https://stepik.org/lesson/24462/step/7?auth=login&thread=solutions&unit=6768 """

# put your python code here
num = int(input())

inh_dict = {}
for i in range(num):
    inh_step = input().split(" : ")  # ключ - класс, значение - его родитель
    if len(inh_step) == 1:
        inh_dict[inh_step[0]] = []
    else:
        inh_dict[inh_step[0]] = list(inh_step[1].split(" "))

list_of_parents = []


def make_list_of_parents(parent, child):
    global list_of_parents
    if child != [] and child in inh_dict.keys():
        list_of_parents += inh_dict[child]
        for child_element in inh_dict[child]:
            make_list_of_parents(parent, child_element)


def is_it_a_parent(parent, child):
    if parent in list_of_parents:
        print("Yes")
    elif parent == child and parent in inh_dict.keys():
        print("Yes")
    else:
        print("No")


num = int(input())
for i in range(num):
    class1, class2 = input().split(" ")
    make_list_of_parents(class1, class2)
    is_it_a_parent(class1, class2)
    list_of_parents = []
