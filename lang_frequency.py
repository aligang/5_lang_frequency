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
    raw_list_of_words_from_text = text_from_file.lower().split()
    list_of_words_from_text = [
        re.sub(
            "\W*(\w+-?\w*)\W*",
            r"\g<0>",
            word
        ) for word in raw_list_of_words_from_text
    ]
    counter_with_words_apearances = Counter(
        list_of_words_from_text
    )
    most_frequent_words_number = 10
    most_frequent_words = dict(
        counter_with_words_apearances.most_common(
            most_frequent_words_number
        )
    )
    return most_frequent_words


def print_pretty_output(most_frequent_words):
    column_shift = 20
    print("Слово {} встречается раз(a)".format(" "*column_shift))
    for frequent_word in most_frequent_words.items():
        word, frequency = frequent_word
        dotted_pointer = (column_shift-len(word)+10)*"."
        print(
            "{:} {:} {:}".format(
                word,
                dotted_pointer,
                frequency
            )
        )


if __name__ == "__main__":
    shell_input = sys.argv
    if len(shell_input) < 2:
        sys.exit(
            "Не указан аргумент - файл."
            "\nПерезапустите скрипт командой в формате "
            "'python3 lang_frequency.py <path to file>'")
    textfile_path = sys.argv[1]
    if not os.path.exists(textfile_path):
        print("Такой файл не существует")
    else:
        text_from_file = load_data(textfile_path)
        most_frequent_words = get_most_frequent_words(text_from_file)
        print(
            "\nCамые часто повторяющиеся слова в файле {}\n".format(
                textfile_path
            )
        )

        print_pretty_output(most_frequent_words)
