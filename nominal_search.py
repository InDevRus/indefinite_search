from general_methods import *
from general_methods import check_word
from itertools import chain


def nominal_search(file, words, length: int,
                   ignore_case: bool = False,
                   line_break: bool = False,
                   sort_by_length: bool = False):
    """
    Using the methods below searches
    for the words nominally in the file.

    Args:
        file (file): File object.
        length (int): Maximum redaction length.
        words (file): File object with words to search in a file.
        ignore_case (bool): If checked, str.casefold() will
            be used before yielding.
        line_break (bool): '-' symbol before newline will
            not be yielded.
        sort_by_length (bool): Output will be sorted by actual length.

    Yields (str): found positions for every word with length
    """

    @check_word
    def nominal_search_for_single_word(current_word: str):
        sequence = chain(
            [0], *map(lambda number: (-number, number), range(1, length + 1)))
        sequence = filter(
            lambda number: number > 0,
            map(lambda number: len(current_word) + number, sequence))
        substrings = chain(*map(
            lambda number: get_substrings_from_file(file, number, line_break),
            sequence))
        yield from yield_occurrences(current_word, length,
                                     substrings, ignore_case,
                                     sort_by_length)

    for word in get_lines_from_file(words):
        file.seek(0)
        yield from nominal_search_for_single_word(word)
