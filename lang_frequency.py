from sys import argv
from os import path
import string
from collections import Counter


def load_data(filepath):
    if not path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file:
        raw_file = file.read()
        text_without_punctuation = raw_file.translate(str.maketrans('', '', string.punctuation))
        text_without_numbers = text_without_punctuation.translate(str.maketrans('', '', '1234567890'))
        text_without_spec_signs = text_without_numbers.translate(str.maketrans('', '', '\n\t\r'))
        words_list = text_without_spec_signs.split()
        return words_list


def get_most_frequent_words(text):
    return Counter(text).most_common(30)


if __name__ == '__main__':
    if len(argv) is 1 or len(argv) >= 3:
        print('\nPlease, specify the file for opening. Example: python lang_frequency.py sh.txt\n')
    else:
        words_list_from_text = load_data(argv[1])
        most_common_words_list = get_most_frequent_words(words_list_from_text)
        print('The thirty most frequent words in the text (in descending order)')
        for num, item in enumerate(most_common_words_list, 1):
            print('{}. {}'.format(num, item[0]))
