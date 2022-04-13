import requests

with open("data/numbers_facts.txt") as numbers, open("data/result_facts.txt", "w") as result:
    for number in numbers:
        url = f"http://numbersapi.com/{number[:-1]}/math?json=true"
        fact_type = "Interesting" if requests.get(url).json()["found"] else "Boring"
        result.write(f"{fact_type}\n")