import requests, re
pattern = r"<(a|script)(.*?)href(.*?)=(\'|\")((.*?:\/\/)|)([^\.].*?)(\:|\/|\'|\")"
urls = {item[6] for item in re.findall(pattern, requests.get("http://pastebin.com/raw/7543p0ns").text)}
with open("Data/assertion.txt") as assertion:
     assertion_list = assertion.read().split()
assert len(assertion_list) == (len(sorted(urls))), f"{len(assertion_list)} {len(sorted(urls))}"
print(True)