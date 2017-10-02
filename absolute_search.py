from general_methods import get_lines_from_file
from general_methods import get_words_from_file
from general_methods import redaction_length
from general_methods import casefold


# TODO: Resolve code duplication.
def absolute_search(file, words, length: int,
                    no_wrap: bool = False,
                    ignore_case: bool = False,
                    line_break: bool = False):
    """
    Using the methods below searches
    for the words absolutely in the file.

    Args:
        file: File object.
        words: File object with words to search in a file.
        length: Expected redaction length.
        no_wrap: New line symbol will not separate an unit word.
        ignore_case: Str.casefold() will
            be used before yielding.
        line_break: '-' symbol before newline will
            not be yielded.

    Returns:
        generator: found positions for every word
    """
    first_word = True
    for word in get_lines_from_file(words):
        file.seek(0)
        if not first_word:
            yield ''
        first_word = False
        if not word.isalpha():
            yield '"{0}" is not a word.'.format(word)
        else:
            yield 'For word "{0}":'.format(word)
            count = 0
            for pair in get_words_from_file(file, no_wrap, line_break):
                to_compare = (pair[0], word)
                if redaction_length(*(to_compare if not ignore_case
                                      else casefold(to_compare))) <= length:
                    yield '    "{0}" in {1} line, {2} position.'.format(*pair)
                    count += 1
            if count > 0:
                yield \
                    ('    Total {0} occurrence' +
                     ('s' if count > 1 else '') +
                     '.').format(count)
            else:
                yield '    No occurrences found.'
