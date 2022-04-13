import json

ENCRYPTED_FILE, KEYS_FILE = "data/Abracadabra.txt", "data/Alphabet.json"
with open(ENCRYPTED_FILE) as enc, open(KEYS_FILE) as keys_file:
    keys = json.load(keys_file)
    for symbol in enc.read():
        if symbol.isalpha():
            print(keys[symbol], end="")
        else:
            print(symbol, end="")
