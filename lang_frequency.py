from sys import argv
from os import path
import string
from collections import Counter
from nltk.corpus import stopwords
from chardet import detect


def detect_encoding(filepath):
    with open(filepath, 'br') as file:
        raw_data = file.read()
    return detect(raw_data)['encoding']


def detect_language_stopwords(list_with_stopwords):
    if stopwords.fileids():
        languages_rate = dict()
        for lang in stopwords.fileids():
            stopwords_set = set(stopwords.words(lang))
            words_set = set(list_with_stopwords)
            common_elements = words_set.intersection(stopwords_set)
            languages_rate[lang] = len(common_elements)
        return languages_rate
    else:
        return None


def detect_language(language_rate_dict):
    return max(language_rate_dict, key=language_rate_dict.get)


def use_stopwords_list(data):
    lang_rate = detect_language_stopwords(data)
    language = detect_language(lang_rate)
    lang_stopwords = stopwords.words(language) if lang_rate and language else None
    if lang_stopwords:
        return [word for word in data if word not in lang_stopwords]
    else:
        return None


def load_data(filepath):
    possible_encoding = detect_encoding(filepath)
    if not path.exists(filepath):
        return None
    with open(filepath, 'r', encoding=possible_encoding) as file:
        return file.read()


def clean_text(raw_file_data):
        text_without_punctuation = raw_file_data.translate(str.maketrans('', '', string.punctuation))
        text_without_numbers = text_without_punctuation.translate(str.maketrans('', '', '1234567890'))
        text_without_spec_signs = text_without_numbers.translate(str.maketrans('', '', '\n\t\r'))
        text_with_stopwords = text_without_spec_signs.lower().split()
        words_list_without_stopwords = use_stopwords_list(text_with_stopwords)
        return words_list_without_stopwords if words_list_without_stopwords else text_with_stopwords


def check_input_arguments(argv):
    if len(argv) is 1 or len(argv) >= 3:
        return True
    else:
        return None


def get_most_frequent_words(text):
    return Counter(text).most_common(10)


if __name__ == '__main__':
    if check_input_arguments(argv):
        print('\nPlease, specify the file for opening. Example: python lang_frequency.py test.txt\n')
    else:
        load_raw_text = load_data(argv[1])
        cleaned_text = clean_text(load_raw_text)
        most_common_words_list = get_most_frequent_words(cleaned_text)
        print('The ten most frequent words in the text (in descending order)')
        for num, item in enumerate(most_common_words_list, 1):
            print('{}. {}'.format(num, item[0]))
