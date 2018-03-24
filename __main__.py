import argparse
import sys
from functools import wraps
from io import StringIO

from logic.absolute_search import absolute_search
from logic.nominal_search import nominal_search


def make_border(func, string: str = None):
    @wraps(func)
    def wrapped(*args):
        print(string)
        print('')
        func(*args)
        print('')

    return wrapped


def perform(gen):
    count = 0
    for line in gen:
        count += 1
        print(line)
    if count == 0:
        print('The word list is empty.')


def define_arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
            description='Reads the text (from file, parameter or STDIN)'
                        'and set of words, then searches for these words '
                        'in text.')

    absolute_search_group = parser.add_mutually_exclusive_group(required=False)
    absolute_search_group.add_argument('-a', '--disable_absolute_search',
                                       help='replace absolute search with '
                                            'nominal',
                                       action='store_true')
    absolute_search_group.add_argument('-r', '--no_wrap',
                                       help='when performing absolute search' +
                                            'do not use line break as word '
                                            'separator',
                                       action='store_true')
    parser.add_argument('-n', '--enable_nominal_search',
                        help='enable nominal search',
                        action='store_true')

    text_group = parser.add_mutually_exclusive_group(required=False)
    text_group.add_argument('-t', '--text', type=str,
                            help='text', metavar='text')
    text_group.add_argument('-tf', '--text_file',
                            help="text file's path", metavar='path')

    word_group = parser.add_mutually_exclusive_group(required=False)
    word_group.add_argument('-w', '--words', nargs='+',
                            help='list of words', metavar='words')
    word_group.add_argument('-wf', '--words_file',
                            help="words file's path", metavar='path')

    parser.add_argument('-i', '--ignore_case', action='store_true',
                        help='ignore case case while searching ' +
                             'using str.casefold() method')
    parser.add_argument('-b', '--line_break', action='store_true',
                        help='end line symbols (line breaking minuses) ' +
                             'will be deleted from text')
    parser.add_argument('-s', '--sort', action='store_true',
                        help='output will be sorted by actual redaction '
                             'length')

    compare_group = parser.add_mutually_exclusive_group()
    compare_group.add_argument('-m', '--match',
                               help='exactly match every word ' +
                                    '(does not affect case ignoring)',
                               action='store_true')
    compare_group.add_argument('-l', '--length',
                               help='change redaction length (1 is default)',
                               type=int, metavar='n', default=1)
    return parser


def main():
    arguments = define_arguments().parse_args()
    if (arguments.text is arguments.text_file is
            arguments.words is arguments.words_file is None):
        print('No text (or text file link) and' +
              ' no word list (or word list file link) found.',
              file=sys.stderr)
        sys.exit(2)

    if arguments.length <= 0:
        print('Length parameter must be positive.', file=sys.stderr)
        sys.exit(2)

    if arguments.text is not None:
        text_file = StringIO(arguments.text)
    elif arguments.text_file is not None:
        text_file = arguments.text_file
    else:
        text_file = sys.stdin

    if arguments.words is not None:
        words_file = StringIO('\n'.join(arguments.words))
    elif arguments.words_file is not None:
        words_file = arguments.words_file
    else:
        words_file = sys.stdin

    search_arguments = [arguments.length if not arguments.match else 0,
                        arguments.no_wrap,
                        arguments.ignore_case,
                        arguments.line_break,
                        arguments.sort]

    with (open(text_file, encoding='utf-8') if isinstance(text_file, str)
          else text_file) as text_file:
        with (open(words_file, encoding='utf-8') if isinstance(words_file,
                                                               str)
              else words_file) as words_file:
            if not arguments.disable_absolute_search:
                generator = absolute_search(text_file, words_file,
                                            *search_arguments)
                if arguments.enable_nominal_search:
                    make_border(perform, 'Absolute search.')(generator)
                else:
                    perform(generator)

            if (arguments.enable_nominal_search
               or arguments.disable_absolute_search):
                search_arguments.pop(1)
                generator = nominal_search(text_file, words_file,
                                           *search_arguments)
                if not arguments.disable_absolute_search:
                    make_border(perform, 'Nominal search.')(generator)
                else:
                    perform(generator)


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(str(exception), file=sys.stderr)
        sys.exit(1)
