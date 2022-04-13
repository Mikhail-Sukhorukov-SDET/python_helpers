import csv
FILE = "data/tipichnaya_zadacha_analitika.csv"


def get_unique_actions_for_each_user(document, place_action: tuple):
    with open(document, encoding='utf-8') as data:
        actions, users, users_actions = {}, set(), set()
        for action in csv.DictReader(data, delimiter=','):
            user_action = action["Пользователь"] + action["Действие"]
            if action["Контекст: место вызова"] in place_action and user_action not in users_actions:
                users.add(action["Пользователь"])
                users_actions.add(user_action)
                actions[action["Действие"]] = actions.get(action["Действие"], 0) + 1
    users = len(users)
    return [(key, actions[key], round(actions[key] / users * 100, 2)) for key in actions]


def get_sorted_actions(actions, field=2, reverse=False):
    return sorted(actions, key=lambda x: x[field], reverse=reverse)


def get_sorted_actions_by_value(actions, actions_count, reverse=False):
    return get_sorted_actions(actions, reverse=reverse)[:actions_count]


def get_sorted_actions_by_percent(actions, percent, reverse=False):
    actions = sorted([item for item in actions if item[2] < percent])
    return actions


tp_actions = get_unique_actions_for_each_user(FILE, ("Панель инструментов",))
most_common_10_actions = get_sorted_actions_by_value(tp_actions, 10, reverse=True)

print("10 самых популярных действий из панели инструментов:")
print(*most_common_10_actions, sep="\n")
print()
print("Действия из панели инструментов которые нажимает менее 10 % пользователей:")
print(*sorted([item for item in tp_actions if item[2] < 10], key=lambda x: x[2], reverse=True), sep="\n")
