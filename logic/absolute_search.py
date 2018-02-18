from logic.general import *


def absolute_search(file, words, length: int,
                    no_wrap: bool = False,
                    ignore_case: bool = False,
                    line_break: bool = False,
                    sort_by_length: bool = False):
    """
    Using the methods below searches
    for the words absolutely in the file.

    Args:
        file (file): File object.
        words (file): File object with words to search in a file.
        length (int): Expected redaction length.
        no_wrap (bool): New line symbol will not separate an unit word.
        ignore_case (bool): Str.casefold() will
            be used before comparing.
        line_break (bool): '-' symbol before newline will
            not be yielded.
        sort_by_length (bool): Output will be sorted by actual length.

    Yields (str): found positions for every word.
    """

    @check_word
    def absolute_search_for_single_word(current_word: str):
        subjects = get_words_from_file(file, no_wrap, line_break)
        yield from yield_occurrences(current_word, length,
                                     subjects, ignore_case,
                                     sort_by_length)

    for word in get_lines_from_file(words):
        file.seek(0)
        yield from absolute_search_for_single_word(word)
