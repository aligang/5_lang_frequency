#!/usr/bin/env python3


import re
import sys
import os
from collections import Counter


def load_data(textfile_path):
    with open(textfile_path, "r") as file_contaning_text:
        text_from_file = file_contaning_text.read()
    return text_from_file


def get_most_frequent_words(text_from_file):
    raw_list_of_words_from_text = text_from_file.split()
    list_of_words_from_text = [
        re.sub(
            "(\W*)(\w+[-]*\w*)(\W*)",
            r'\2',
            word
        ) for word in raw_list_of_words_from_text
    ]
    decapitalized_list_of_words_from_text = [
        word.lower() for word in list_of_words_from_text
    ]
    dict_with_words_apearances = Counter(
        decapitalized_list_of_words_from_text
    )
    most_frequent_words = dict_with_words_apearances.most_common(10)
    return most_frequent_words


def get_pretty_output(most_frequent_words):
    for word in most_frequent_words:
        print(
            "Слово    {:10}    встречается   {:<5}  раз(a)".format(
                word[0],
                word[1]
            )
        )


if __name__ == "__main__":
    textfile_path = sys.argv[1]
    if not os.path.exists(textfile_path):
        print("Такой файл не существует")
    else:
        text_from_file = load_data(textfile_path)
        most_frequent_words = get_most_frequent_words(text_from_file)
        print("самые часто повторяющиеся слова в файле {}".format(textfile_path))
        get_pretty_output(most_frequent_words)
