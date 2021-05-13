from string import punctuation


def longest_word_in_file(file_name):
    with open(file_name,  encoding='utf-8') as f:
        l = []
        for word in f.read().split():
            word = word.strip(punctuation)
            l.append(word)
        return sorted(l, key=lambda x: len(x))[-1]


print(longest_word_in_file("dataset_3380_5.txt"))
