def caesar_cipher(row, step, lang='ru', cipher=True):
    result_row = ''
    for symbol in row:
        if symbol.isalpha():
            if lang == 'ru':
                if 1072 <= ord(symbol) <= 1103:
                    index = 1072 + (ord(symbol) - 1072 + step) % 32 if cipher else 1072 + (
                            ord(symbol) - 1072 - step) % 32
                    result_row += chr(index)
                elif 1040 <= ord(symbol) <= 1071:
                    index = 1040 + (ord(symbol) - 1040 + step) % 32 if cipher else 1040 + (
                            ord(symbol) - 1040 - step) % 32
                    result_row += chr(index)
            elif lang == 'en':
                if 97 <= ord(symbol) <= 122:
                    index = 97 + (ord(symbol) - 97 + step) % 26 if cipher else 97 + (ord(symbol) - 97 - step) % 26
                    result_row += chr(index)
                elif 65 <= ord(symbol) <= 90:
                    index = 65 + (ord(symbol) - 65 + step) % 26 if cipher else 65 + (ord(symbol) - 65 - step) % 26
                    result_row += chr(index)
        else:
            result_row += symbol
    return result_row


assert caesar_cipher('Блажен, кто верует, тепло ему на свете!', 10) == 'Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!'
assert caesar_cipher('To be, or not to be, that is the question!', 17,
                     lang='en') == 'Kf sv, fi efk kf sv, kyrk zj kyv hlvjkzfe!'
assert caesar_cipher('Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.', 7,
                     cipher=False) == 'Скупой теряет все, желая все достать.'
assert caesar_cipher('Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.', 25, lang='en',
                     cipher=False) == 'The grass is always greener on the other side of the fence.'

for i in range(0, 26):
    print(caesar_cipher('Hawnj pk swhg xabkna ukq nqj.', i, lang='en', cipher=False))

first_case = 'Day, mice. "Year" is a mistake!'
first_answer = []
for string in first_case:
    first_answer.append(caesar_cipher(string, len(string.strip(",").strip('!').strip('"').strip('.'))))

assert " ".join(first_answer) == 'Gdb, qmgi. "Ciev" ku b tpzahrl!'

second_case = 'my name is Python!'
second_answer = []
for string in first_case:
    second_answer.append(caesar_cipher(string, len(string.strip(",").strip('!').strip('"').strip('.'))))

assert " ".join(second_answer) == 'oa reqi ku Veznut!'

third_case = 'To be, or not to be, that is the question'
third_answer = []
for string in first_case:
    third_answer.append(caesar_cipher(string, len(string.strip(",").strip('!').strip('"').strip('.'))))

assert " ".join(third_answer) == 'Vq dg, qt qrw vq dg, xlex ku wkh ycmabqwv'
