import argparse
from io import StringIO
from sys import stdin, stderr
from nominal_search import nominal_search
from absolute_search import absolute_search
from frames import make_border


def perform(gen):
    count = 0
    for line in gen:
        count += 1
        print(line)
    if count == 0:
        print('The word list is empty.')


# Argument definition.
parser = argparse.ArgumentParser(
    description='Reads the text (from file, parameter or STDIN)' +
    'and set of words, then searches for these words in text.'
)

absolute_search_group = parser.add_mutually_exclusive_group(required=False)
absolute_search_group.add_argument('-a', '--disable_absolute_search',
                                   help='replace absolute search with nominal',
                                   action='store_true')
absolute_search_group.add_argument('-r', '--no_wrap',
                                   help='when performing absolute search' +
                                   'do not use line break as word separator',
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

compare_group = parser.add_mutually_exclusive_group()
compare_group.add_argument('-m', '--match',
                           help='exactly match every word ' +
                                '(does not affect case ignoring)',
                           action='store_true')
compare_group.add_argument('-l', '--length',
                           help='change redaction length (1 is default)',
                           type=int, metavar='n', default=1)

# Argument initialization.
arguments = parser.parse_args()
if arguments.text is arguments.text_file is\
        arguments.words is arguments.words_file is None:
    print('No text (or text file link) and' +
          ' no word list (or word list file link) found.',
          file=stderr)
    exit(2)

if arguments.length <= 0:
    print('Length parameter must be positive.', file=stderr)
    exit(2)

text_file = words_file = None
try:
    # Argument analyzing.
    # Creating file object of text from argument.
    if arguments.text is not None:
        text_file = StringIO(arguments.text)
    # If no text, trying open file.
    elif arguments.text_file is not None:
        try:
            text_file = open(arguments.text_file, encoding='utf-8')
        except FileNotFoundError:
            print('There is no file, called {}.'.format(arguments.text_file),
                  file=stderr)
            exit(2)
    # And finally, trying read text from STDIN.
    else:
        text_file = StringIO(stdin.read())

    # Same actions for word list.
    if arguments.words is not None:
        words_file = StringIO('\n'.join(arguments.words))
    elif arguments.words_file is not None:
        try:
            words_file = open(arguments.words_file, encoding='utf-8')
        except FileNotFoundError:
            print('There is no file, called {}.'.format(arguments.words_file),
                  file=stderr)
            exit(2)
    else:
        words_file = StringIO(stdin.read())

    # Absolute search
    if not arguments.disable_absolute_search:
        generator =\
            absolute_search(text_file,
                            words_file,
                            arguments.length if not arguments.match else 0,
                            arguments.no_wrap,
                            arguments.ignore_case,
                            arguments.line_break)
        if arguments.enable_nominal_search:
            make_border('Absolute search.', perform, generator)
        else:
            perform(generator)

    # Nominal search
    if arguments.enable_nominal_search or arguments.disable_absolute_search:
        generator = nominal_search(text_file,
                                   words_file,
                                   arguments.length if not
                                   arguments.match else 0,
                                   arguments.ignore_case,
                                   arguments.line_break)
        if not arguments.disable_absolute_search:
            make_border('Nominal search.', perform, generator)
        else:
            perform(generator)
# If any error will appear, we must close any opened files.
finally:
    for file in (text_file, words_file):
        if file is not None:
            file.close()
