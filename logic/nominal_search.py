from logic import general
from operator import add, lt
from functools import partial
from utilities.iterable import Iterable


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

    @general.check_word
    def nominal_search_for_single_word(current_word: str):
        sequence = (Iterable([0])
                    .concat(Iterable(range(1, length + 1))
                            .chain(lambda number: (-number, number)))
                    .map(partial(add, len(current_word)))
                    .filter(partial(lt, 0)))
        substrings = (Iterable(sequence)
                      .chain(lambda number:
                             general.get_substrings_from_file(file,
                                                              number,
                                                              line_break)))

        yield from general.yield_occurrences(current_word, length,
                                             substrings, ignore_case,
                                             sort_by_length)

    for word in general.get_lines_from_file(words):
        file.seek(0)
        yield from nominal_search_for_single_word(word)
