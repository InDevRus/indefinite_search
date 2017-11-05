def add_whitespaces(count: int = 4):
    def decorator(generator):
        def wrapped(*args):
            yield from map(lambda line: ' ' * count + line,
                           generator(*args))
        return wrapped
    return decorator


@add_whitespaces()
def yield_occurrences(func, sequence):
    count = 0
    for pair in sequence:
        if func(pair[0]):
            yield '"{0}" in {1} position.'.format(*pair)
            count += 1
    yield ('Total {0} occurrence' +
           ('s' if count > 1 else '') +
           '.').format(count)


def check_length(func):
    def wrapped(first: str, second: str):
        if first == second:
            return 0
        else:
            return func(first, second)
    return wrapped


def make_border(string, func, *args):
    print(string)
    print('')
    func(*args)
    print('')
