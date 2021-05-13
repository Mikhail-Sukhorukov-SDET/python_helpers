import json


def the_best_manager(file_name):
    with open(file_name, encoding='utf-8') as f:
        res = {}
        data = json.load(f)
        for i in range(len(data)):
            res[data[i]["manager"]["first_name"] + " " + data[i]["manager"]["last_name"]] = 0
            for car in data[i]["cars"]:
                res[data[i]["manager"]["first_name"] + " " + data[i]["manager"]["last_name"]] += car["price"]

        return sorted(res.items(), key=lambda value: value[1])[-1]


print(the_best_manager("manager_sales.json"))