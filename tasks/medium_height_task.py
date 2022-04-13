m = {}
with open("tasks/dataset_3380_5.txt") as file:
    for row in file:
        row = row.split()
        class_key = int(row[0])
        if int(class_key) not in m.keys():
            m[class_key] = [0, 0]
        m[class_key][0] += int(row[2])
        m[class_key][1] += 1
keys = sorted(m.keys())
for key in range(1, len(keys)+1):
    if key not in m.keys():
        print(f"{key} -")
    else:
        print(key, m[key][0]/m[key][1])
