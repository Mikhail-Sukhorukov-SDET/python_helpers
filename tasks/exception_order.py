""" https://stepik.org/lesson/24463/step/7?unit=6771 """
inh = {}


def find_parents(parents, passed):
    if parents is []:
        return False
    for parent in parents:
        if parent in passed:
            return True
        else:
            if find_parents(inh[parent], passed):
                return True


for i in range(int(input())):
    row = input().split(" ")
    child = row[0]
    parents = row[2:]
    inh[child] = parents
# print(inh)

data2 = [input() for i in range(int(input()))]
# print(data2)
passed = [data2[0]]
for i in range(1, len(data2)):
    if find_parents(inh[data2[i]], passed):
        print(data2[i])
    passed.append(data2[i])

