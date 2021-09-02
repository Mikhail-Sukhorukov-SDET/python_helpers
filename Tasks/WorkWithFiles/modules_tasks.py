"""
import datetime

year, month, day = input().split(" ")
d = datetime.date(int(year), int(month), int(day))
d += datetime.timedelta(days=int(input()))
print(d.year, d.month, d.day)
"""

import simplecrypt

ENCRYPTED_FILE = "Data/encrypted.bin"
PASSWORDS_FILE = "Data/passwords.txt"
with open(ENCRYPTED_FILE, "rb") as inp:
    encrypted = inp.read()

with open(PASSWORDS_FILE) as passwords:
    for password in passwords:
        try:
            decrypted = simplecrypt.decrypt(password.strip(), encrypted)
            print(decrypted)
            break
        except simplecrypt.DecryptionException:
            print(password)
