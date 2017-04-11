import argparse
import sys
import textwrap
import re
from os import path
import collections


RUSSIAN_STOPWORDS_LIST = ['и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как',
                          'а', 'то', 'все', 'она', 'так', 'его', 'но', 'да', 'ты', 'к', 'у',
                          'же', 'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было', 'вот',
                          'от', 'меня', 'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда', 'даже',
                          'ну', 'вдруг', 'ли', 'если', 'уже', 'или', 'ни', 'быть', 'был', 'него',
                          'до', 'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там', 'потом', 'себя',
                          'ничего', 'ей', 'может', 'они', 'тут', 'где', 'есть', 'надо', 'ней', 'для',
                          'мы', 'тебя', 'их', 'чем', 'была', 'сам', 'чтоб', 'без', 'будто', 'чего',
                          'раз', 'тоже', 'себе', 'под', 'будет', 'ж', 'тогда', 'кто', 'этот', 'того',
                          'потому', 'этого', 'какой', 'совсем', 'ним', 'здесь', 'этом', 'один', 'почти',
                          'мой', 'тем', 'чтобы', 'нее', 'сейчас', 'были', 'куда', 'зачем', 'всех',
                          'никогда', 'можно', 'при', 'наконец', 'два', 'об', 'другой', 'хоть', 'после',
                          'над', 'больше', 'тот', 'через', 'эти', 'нас', 'про', 'всего', 'них', 'какая',
                          'много', 'разве', 'три', 'эту', 'моя', 'впрочем', 'хорошо', 'свою', 'этой',
                          'перед', 'иногда', 'лучше', 'чуть', 'том', 'нельзя', 'такой', 'им', 'более',
                          'всегда', 'конечно', 'всю', 'между']


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)

    def check_python_version(self):
        if sys.version_info < (3, 5):
            self.print_help()
            raise SystemExit('\nSorry, this code needs Python 3.5 or higher\n')


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


def load_data(filepath):
    if not path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def clean_text(text):
        words_and_numbers_list = re.findall('\w+', text.lower().strip())
        words_list = [word for word in words_and_numbers_list if not word.isdigit()]
        words_list_without_stopwords = [word for word in words_list if word not in RUSSIAN_STOPWORDS_LIST]
        return words_list_without_stopwords


def get_most_frequent_words(text, number_of_words_to_show):
    return collections.Counter(text).most_common(number_of_words_to_show)


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
