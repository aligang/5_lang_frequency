#!/usr/bin/env python3


import re
import sys
import os
from collections import Counter


def load_data(textfile_path):
    with open(textfile_path, "r") as file_contaning_text:
        source_text = file_contaning_text.read()
    return source_text


def get_most_frequent_words(source_text):
    lowercase_text = source_text.lower()
    list_of_words = re.findall("\w+-?\w*", lowercase_text)
    counter_with_words_apearances = Counter(
        list_of_words
    )
    most_frequent_words_number = 10
    most_frequent_words = counter_with_words_apearances.most_common(
        most_frequent_words_number
    )
    return most_frequent_words


def print_pretty_output(most_frequent_words):
    column_width = 20
    text_shift = 13
    print("Слово {} встречается раз(a)".format(" "*column_width))
    for word, frequency in most_frequent_words:
        dotted_pointer = (column_width-len(word)+text_shift)*"."
        print(
            "{:} {:} {:}".format(
                word,
                dotted_pointer,
                frequency
            )
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(
            "Не указан аргумент - файл."
            "\nПерезапустите скрипт командой в формате "
            "'python3 lang_frequency.py <path to file>'")
    textfile_path = sys.argv[1]
    if not os.path.exists(textfile_path):
        print("Такой файл не существует")
    else:
        source_text = load_data(textfile_path)
        most_frequent_words = get_most_frequent_words(source_text)
        print(
            "\nCамые часто повторяющиеся слова в файле {}\n".format(
                textfile_path
            )
        )
        print_pretty_output(most_frequent_words)
