from io import StringIO


def assert_function(func, iterable=False):
    """
    Universal function
    assertion decorator.
    """
    def decorator(test_method):
        def wrapped(self):
            for args in test_method(self):
                result = func(*args[:-1])
                result = tuple(result) if iterable else result
                self.assertEqual(result, args[-1])
        return wrapped
    return decorator


def wrap_string_in_io(position: int = 0):
    def decorator(test_method):
        def wrapped(self):
            data = test_method(self)
            for args in data:
                args[position] = StringIO(args[position])
            return data
        return wrapped
    return decorator


def append_arguments(*args):
    def decorator(test_method):
        def wrapped(self):
            data = test_method(self)
            for arguments in data:
                for argument in args:
                    arguments.insert(-1, argument)
            return data
        return wrapped
    return decorator


def wrap_list_in_io(position: int = 1):
    def decorator(test_method):
        def wrapped(self):
            data = test_method(self)
            for args in data:
                args[position] =\
                    StringIO('\n'.join(args[position]))
            return data
        return wrapped
    return decorator
