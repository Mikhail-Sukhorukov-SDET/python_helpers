"""
import datetime

year, month, day = input().split(" ")
d = datetime.date(int(year), int(month), int(day))
d += datetime.timedelta(days=int(input()))
print(d.year, d.month, d.day)
"""

import simplecrypt

ENCRYPTED_FILE = "encrypted.bin"
PASSWORDS_FILE = "passwords.txt"
with open(ENCRYPTED_FILE, "rb") as inp:
    encrypted = inp.read()
    print(encrypted)

with open(PASSWORDS_FILE) as passwords:
    for password in passwords:
        try:
            decrypted = simplecrypt.decrypt(password.strip(), encrypted)
            print(decrypted)
        except simplecrypt.DecryptionException:
            print(password)
