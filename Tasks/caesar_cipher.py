UNICODE_POINTS = {
        "ru": {
            "Low": {
                "Start": 1072,
                "End": 1103
            },
            "Up": {
                "Start": 1040,
                "End": 1071
            },
            "Count": 32
        },
        "en": {
            "Low": {
                "Start": 97,
                "End": 122
            },
            "Up": {
                "Start": 65,
                "End": 90
            },
            "Count": 26
        }
    }


TEST_DATA = (
    {
        "Decoded": "Блажен, кто верует, тепло ему на свете!",
        "Encoded": "Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!"
    },
    {
        "Decoded": "To be, or not to be, that is the question!",
        "Encoded": "Kf sv, fi efk kf sv, kyrk zj kyv hlvjkzfe!"
    },
    {
        "Decoded": "Скупой теряет все, желая все достать.",
        "Encoded": "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
    },
    {
        "Decoded": "The grass is always greener on the other side of the fence.",
        "Encoded": "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
    },
    {
        "Decoded": None,
        "Encoded": "Hawnj pk swhg xabkna ukq nqj."
    },
    {
        "Decoded": "Day, mice. \"Year\" is a mistake!",
        "Encoded": "Gdb, qmgi. \"Ciev\" ku b tpzahrl!"
    },
    {
        "Decoded": "my name is Python!",
        "Encoded": "oa reqi ku Veznut!"
    },
    {
        "Decoded": "To be, or not to be, that is the question",
        "Encoded": "Vq dg, qt qrw vq dg, xlex ku wkh ycmabqwv"
    },
)


def caesar_cipher(row: str, step: int, lang="ru", cipher=True):
    result_row, point = "", UNICODE_POINTS[lang]
    low, up, count = point["Low"], point["Up"], point["Count"]
    register = low
    for symbol in row:
        if symbol.isalpha():
            if low["Start"] <= ord(symbol) <= low["End"]:
                register = low
            elif up["Start"] <= ord(symbol) <= up["End"]:
                register = up
            symbol = chr(get_index(symbol, step, register, count, cipher))
        result_row += symbol
    return result_row


def get_index(letter: str, step: int, register: dict, count: int, cipher: bool):
    difference = ord(letter) + step if cipher else ord(letter) - step
    return register["Start"] + (difference - register["Start"]) % count


assert caesar_cipher(TEST_DATA[0]["Decoded"], 10) == TEST_DATA[0]["Encoded"]
assert caesar_cipher(TEST_DATA[1]["Decoded"], 17, lang='en') == TEST_DATA[1]["Encoded"]
assert caesar_cipher(TEST_DATA[2]["Encoded"], 7, cipher=False) == TEST_DATA[2]["Decoded"]
assert caesar_cipher(TEST_DATA[3]["Encoded"], 25, lang='en', cipher=False) == TEST_DATA[3]["Decoded"]

for i in range(0, 26):
    print(caesar_cipher(TEST_DATA[4]["Encoded"], i, lang='en', cipher=False))


for case in TEST_DATA[-3:]:
    decoded_row, encoded_row, answer = case["Decoded"].split(), case["Encoded"], []
    for word in decoded_row:
        word_len = len(word.strip(",").strip('!').strip('"').strip('.'))
        answer.append(caesar_cipher(word, word_len, lang="en"))
    assert " ".join(answer) == encoded_row
