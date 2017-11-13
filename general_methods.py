from functools import lru_cache


def check_length(func):
    def wrapped(first: str, second: str):
        if first == second:
            return 0
        else:
            return func(first, second)

    return wrapped


@lru_cache(maxsize=1024)
@check_length
def redaction_length(first: str, second: str) -> int:
    """
    Calculates the redaction length between two strings.

    Args:
        first (str): First string.
        second (str): second string.

    Returns (int): The redaction length between them.
    """
    table = {}

    def f(x: int, y: int):
        return table[(x, y)]
    for first_length in range(0, len(first) + 1):
        for second_length in range(0, len(second) + 1):
            if first_length * second_length == 0:
                result = max(first_length, second_length)
            else:
                result = f(first_length - 1, second_length - 1) if \
                    first[first_length - 1] == second[second_length - 1] else\
                    1 + min(
                        f(first_length - 1, second_length),
                        f(first_length - 1, second_length - 1),
                        f(first_length, second_length - 1))
            table[(first_length, second_length)] = result

    return table[(len(first), len(second))]


def get_words_from_file(file, no_wrap: bool = False,
                        line_break: bool = False):
    """
    Gets words from file.

    Args:
        file (file): File object.
        line_break (bool): '-' symbol before newline will
            not be yielded.
        no_wrap (bool): line breaks symbols
            will not separate an unite word

    Notes:
        line break symbols will be deleted from words anyway

    Yields (tuple): Words from file with positions in it.
    """
    word = ''
    begin_position = position = 0
    begin_line = line = 1

    def reset():
        nonlocal begin_position, word, begin_line
        word = ''
        begin_position = position
        begin_line = line

    def is_separator(subject: str) -> bool:
        return not subject.isalpha() and subject not in ('\n', '-')

    def read_symbol() -> str:
        nonlocal position, line
        position += 1
        current = file.read(1)
        if current == '\n':
            update_line_count()
        return current

    def update_line_count():
        nonlocal position, line
        line += 1
        position = 0

    while True:
        symbol = read_symbol()
        if symbol == '':
            if len(word) > 0:
                yield word, begin_line, begin_position
            break
        elif symbol == '-' and line_break:
            next_symbol = read_symbol()
            if next_symbol == '\n':
                pass
            else:
                if len(word) > 0:
                    yield word, begin_line, begin_position
                reset()
                word += next_symbol
        elif is_separator(symbol) or (symbol == '\n' and not no_wrap):
            if len(word) > 0:
                yield word, begin_line, begin_position
            reset()
        elif symbol == '\n':
            if len(word) == 0:
                reset()
        else:
            word += symbol


def get_lines_from_file(file):
    """
    Reads every line in file and
    returns every line.

    Args:
        file (file): File object.

    Yields (str): Lines with deleted newline symbol.
    """
    file.seek(0)
    for line in file:
        line = line.replace('\n', '')
        if len(line) >= 1 and line[-1] == '\r':
            line = line[:-1]
        yield line


def get_substrings_from_file(file, length: int,
                             line_break: bool = False):
    """
    Iterates over the text file and
    returns every substring with given length.

    Args:
        file (file): File object.
        length (int): Expected length of substrings.
        line_break (bool): '-' symbol before newline will
            not be yielded.

    Yields (tuple): Tuple of substrings and position.
    """
    file.seek(0)
    position = -1
    line = 1

    def read_symbol() -> str:
        nonlocal position, line
        position += 1
        current = file.read(1)
        if current == '\n':
            update_line_count()
        return current

    def append_and_cut(self, appendix):
        if isinstance(self, str):
            result = self + appendix
        else:
            result = self
            result.append(appendix)
        return result[-length:]

    def update_line_count():
        nonlocal position, line
        line += 1
        position = -1

    substring = ''
    positions = []
    while length > 0:
        symbol = read_symbol()
        if symbol == '':
            break
        if line_break and symbol == '-':
            next_symbol = read_symbol()
            if next_symbol == '\n':
                pass
            elif next_symbol == '':
                substring = append_and_cut(substring, symbol)
                positions = append_and_cut(positions, (line, position))
                if len(substring) == length:
                    yield substring, (*positions[0])
            else:
                difference = 1
                for part in (symbol, next_symbol):
                    substring = append_and_cut(substring, part)
                    positions = append_and_cut(
                        positions, (line, position - difference))
                    difference = 0
                    if len(substring) == length:
                        yield substring, (*positions[0])
        else:
            if symbol == '\n':
                continue
            substring = append_and_cut(substring, symbol)
            positions = append_and_cut(positions, (line, position))
            if len(substring) == length:
                yield substring, (*positions[0])


def add_whitespaces(count: int = 4):
    def decorator(generator):
        def wrapped(*args):
            yield from map(lambda line: ' ' * count + line,
                           generator(*args))

        return wrapped

    return decorator


def check_word(func):
    def wrapped(word: str, *args):
        if not word.replace('-', '').isalpha():
            yield '"{0}" is not a word.'.format(word)
        else:
            yield 'For word "{0}":'.format(word)
            yield from func(word, *args)

    return wrapped


@add_whitespaces()
def yield_occurrences(word: str, length: int, sequence, ignore_case: bool,
                      sort_by_length: bool = False):
    def yield_answers():
        for tokens in sequence:
            substring = tokens[0]
            substring = substring if not ignore_case else substring.casefold()
            actual_length = redaction_length(word, substring)
            if actual_length <= length:
                yield (*tokens, actual_length)

    word = word if not ignore_case else word.casefold()
    pattern = '"{0}" in {1} line, {2} position with {3} length.'
    count = 0
    tetras = yield_answers()
    tetras = tetras if not sort_by_length else sorted(tetras, key=
    lambda tetra: tetra[-1])
    for answers in tetras:
        yield pattern.format(*answers)
        count += 1
    if count > 0:
        yield \
            ('Total {0} occurrence' +
             ('s' if count > 1 else '') +
             '.').format(count)
    else:
        yield 'No occurrences found.'
