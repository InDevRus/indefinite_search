from general_methods import get_lines_from_file
from general_methods import get_substrings_from_file
from general_methods import redaction_length
from general_methods import casefold


# TODO: Resolve code duplication.
def nominal_search(file, words, length: int,
                   ignore_case: bool = False,
                   line_break: bool = False):
    """
    Using the methods below searches
    for the words nominally in the file.

    Args:
        file: File object.
        length: Maximum redaction length.
        words: File object with words to search in a file.
        ignore_case: If checked, str.casefold() will
            be used before yielding.
        line_break: '-' symbol before newline will
            not be yielded.

    Returns:
        generator: found positions for every word
    """
    first_word = True
    for word in get_lines_from_file(words):
        if not first_word:
            yield ''
        first_word = False
        if not word.isalpha():
            yield '"{0}" is not a word.'.format(word)
        else:
            yield 'For word "{0}":'.format(word)
            sequence = \
                [0] + [(-1)**a*b for b in range(1, length + 1) for a in (1, 2)]
            count = 0
            for element in sequence:
                file.seek(0)
                for pair in get_substrings_from_file(
                        file, len(word) + element, line_break):
                    to_compare = (pair[0], word)
                    if redaction_length(
                            *(to_compare if not ignore_case
                              else casefold(to_compare))) <= length:
                        yield '    "{0}" in {1} line, {2} position.'\
                            .format(*pair)
                        count += 1
            if count > 0:
                yield \
                    ('    Total {0} occurrence' +
                     ('s' if count > 1 else '') +
                     '.').format(count)
            else:
                yield '    No occurrences found.'
