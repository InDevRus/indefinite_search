from io import StringIO


def assert_equal(func, iterable=False, out_type=tuple):
    def decorator(test_method):
        def wrapped(self):
            for args in test_method(self):
                result = func(*args[:-1])
                result = out_type(result) if iterable else result
                self.assertEqual(result, args[-1])
        return wrapped
    return decorator


def assert_different(func, iterable=False):
    def decorator(test_method):
        def wrapped(self):
            for args in test_method(self):
                result = func(*args[:-1])
                result = (result,) if iterable else result
                self.assertNotEqual(result, args[-1])
        return wrapped
    return decorator


def assert_raises(func, exception, regex: str = None,
                  iterable=True, out_type=tuple):
    def decorator(test_method):
        def wrapped(self):
            for args in test_method(self):
                with (self.assertRaises(exception) if regex is None else
                      self.assertRaisesRegex(exception, regex)):
                    func(*args) if not iterable else out_type(func(*args))

        return wrapped

    return decorator


def append_arguments(*args, position: int = -1):
    def decorator(test_method):
        def wrapped(self):
            data = test_method(self)
            for arguments in data:
                for argument in args:
                    arguments.insert(position, argument)
            return data
        return wrapped
    return decorator


def wrap_string_in_io(position: int = 0, iterable: bool = False):
    def decorator(test_method):
        def wrapped(self):
            data = test_method(self)
            for args in data:
                if iterable:
                    args[position] = StringIO('\n'.join(args[position]))
                else:
                    args[position] = StringIO(args[position])
            return data
        return wrapped
    return decorator
