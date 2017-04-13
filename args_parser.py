import argparse
import textwrap
import sys


class ConsoleArgsParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(ConsoleArgsParser, self).__init__(*args, **kwargs)
        self.prog = 'Word Frequency counter'
        self.formatter_class = argparse.RawDescriptionHelpFormatter
        self.description = textwrap.dedent('''\
                      Script for count words frequency \n
                      -----------------------------------------------------------------
                      If you want to stop the program press Ctrl+C.
                      ------------------------------------------------------------------
                      This program had been tested on Python 3.5.2.
                      ''')
        self.add_argument('--file', nargs='?',
                          help='Paste full path to file with text,\
                              e.g --file /home/user/documents/shakespeare_sonnets.txt\
                              (default: %(default)s)',
                          type=str, default=None)
        self.add_argument('--num_of_words',
                          help='How many words will be showed in result,\
                              e.g --num_of_words 5',
                          type=int)

    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)

    def check_python_version(self):
        if sys.version_info < (3, 5):
            self.print_help()
            raise SystemExit('\nSorry, this code needs Python 3.5 or higher\n')
