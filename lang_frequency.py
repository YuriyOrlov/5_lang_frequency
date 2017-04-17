import re
from os import path
import collections
from args_parser import ConsoleArgsParser

NUMBER_OF_WORDS_TO_SHOW_BY_DEFAULT = 10

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


def get_most_frequent_words(text, words_list_length):
    return collections.Counter(text).most_common(words_list_length)


if __name__ == '__main__':
    args_parser = ConsoleArgsParser()
    args = args_parser.parse_args()
    loaded_text = load_data(args.file)
    words_list_length = args.num_of_words if args.num_of_words else NUMBER_OF_WORDS_TO_SHOW_BY_DEFAULT
    cleaned_text = clean_text(loaded_text)
    most_common_words_list = get_most_frequent_words(cleaned_text, words_list_length)
    print('\nThe {} most frequent words in the text (in descending order)'.format(words_list_length))
    for num, item in enumerate(most_common_words_list, 1):
        print('{}. {}'.format(num, item[0]))
