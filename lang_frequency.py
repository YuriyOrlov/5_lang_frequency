import argparse
import sys
import textwrap
import re
from os import path
from collections import Counter
from nltk.corpus import stopwords


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)

    def check_python_version(self):
        if sys.version_info < (3, 5):
            self.print_help()
            raise SystemExit('\nSorry, this code needs Python 3.5 or higher\n')


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


def create_parser():
    parser = MyParser(prog='Word Frequency counter', formatter_class=argparse.RawDescriptionHelpFormatter,
                      description=textwrap.dedent('''\
                      Script for count words frequency \n
                      -----------------------------------------------------------------
                      If you want to stop the program press Ctrl+C.
                      ------------------------------------------------------------------
                      This program had been tested on Python 3.5.2.
                      '''))
    parser.add_argument('--file', nargs='?',
                        help='Paste full path to file with text,\
                              e.g --file /home/user/documents/shakespeare_sonnets.txt\
                              (default: %(default)s)',
                        type=str, default=None)

    parser.add_argument('--num_of_words',
                        help='How many words will be showed in result,\
                              e.g --num_of_words 5 \
                              (default: %(default)s)',
                        type=int, default=10)
    return parser


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
    if not path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def clean_text(text_from_file):
        splitted_text_with_numbers = re.findall('\w+', text_from_file.lower().strip())
        splitted_text_without_numbers = [word for word in splitted_text_with_numbers if not word.isdigit()]
        words_list_without_stopwords = use_stopwords_list(splitted_text_without_numbers)
        return words_list_without_stopwords if words_list_without_stopwords else splitted_text_without_numbers


def get_most_frequent_words(text, number_of_words_to_show=10):
    return Counter(text).most_common(number_of_words_to_show)


if __name__ == '__main__':
    parser = create_parser()
    parser.check_python_version()
    args = parser.parse_args()
    loaded_text = load_data(args.file)
    cleaned_text = clean_text(loaded_text)
    most_common_words_list = get_most_frequent_words(cleaned_text, args.num_of_words)
    print('\nThe ten most frequent words in the text (in descending order)')
    for num, item in enumerate(most_common_words_list, 1):
        print('{}. {}'.format(num, item[0]))
