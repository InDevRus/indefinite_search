import unittest
import pathmagic
from tests.test_decorators import *
from itertools import chain
import general_methods


class GeneralMethodsTests(unittest.TestCase):
    @assert_equal(general_methods.redaction_length)
    def test_redaction_length(self):
        data = [('', '', 0), ('a', '', 1), ('123', '321', 2),
                ('cat', 'clone', 4), ('student', 'soldier', 5),
                ('troll', 'roll', 1), ('boil', 'ufo', 4),
                ('Tris', 'this', 2), ('word', 'word', 0)]
        data = map(lambda x: (x, (x[1], x[0], x[2])), data)
        return chain(*data)

    @assert_equal(general_methods.get_lines_from_file, iterable=True)
    @wrap_string_in_io()
    def test_get_lines_from_file(self):
        data = [['134\n54\n\n\na\ne-\n\n',
                 ('134', '54', '', '', 'a', 'e-', '')],
                ['\n67\na\n\n\n\n\nx234',
                 ('', '67', 'a', '', '', '', '', 'x234')]]
        return data

    @assert_equal(general_methods.get_substrings_from_file, iterable=True)
    @append_arguments(True)
    @wrap_string_in_io()
    def test_get_substring_with_line_break(self):
        return [['x-a-r-\n`pb-', 2,
                 (('x-', 1, 0), ('-a', 1, 1), ('a-', 1, 2), ('-r', 1, 3),
                  ('r`', 1, 4), ('`p', 2, 0), ('pb', 2, 1), ('b-', 2, 2))],
                ['x---g', 3, (('x--', 1, 0),
                              ('---', 1, 1),
                              ('--g', 1, 2))],
                ['x+X-ty-\n ro- \nRd2', 2,
                 (('x+', 1, 0), ('+X', 1, 1), ('X-', 1, 2), ('-t', 1, 3),
                  ('ty', 1, 4),
                  ('y ', 1, 5), (' r', 2, 0),
                  ('ro', 2, 1), ('o-', 2, 2), ('- ', 2, 3),
                  (' R', 2, 4), ('Rd', 3, 0), ('d2', 3, 1))],
                ['x+X-ty-\n ro- \nRd2', 1,
                 (('x', 1, 0), ('+', 1, 1), ('X', 1, 2),
                  ('-', 1, 3), ('t', 1, 4), ('y', 1, 5),
                  (' ', 2, 0), ('r', 2, 1), ('o', 2, 2),
                  ('-', 2, 3), (' ', 2, 4), ('R', 3, 0),
                  ('d', 3, 1), ('2', 3, 2))]]

    @assert_equal(general_methods.get_substrings_from_file, iterable=True)
    @wrap_string_in_io()
    def test_get_substring(self):
        return [['a-x-\nb', 2,
                 (('a-', 1, 0), ('-x', 1, 1), ('x-', 1, 2), ('-b', 1, 3))],
                ['123', 2, (('12', 1, 0), ('23', 1, 1))]]

    @assert_equal(general_methods.get_words_from_file, iterable=True)
    @wrap_string_in_io()
    def test_get_words_from_text(self):
        return [['This is my text.',
                 (('This', 1, 0), ('is', 1, 5),
                  ('my', 1, 8), ('text', 1, 11))],
                ['This text is\n separated by \nline breaks' +
                 ' (word wraps)\n', False, False,
                 (('This', 1, 0),
                  ('text', 1, 5),
                  ('is', 1, 10),
                  ('separated', 2, 1),
                  ('by', 2, 11),
                  ('line', 3, 0),
                  ('breaks', 3, 5),
                  ('word', 3, 13),
                  ('wraps', 3, 18))
                 ],
                ['This text is \nsepara\nted by \n line breaks',
                 True, False,
                 (('This', 1, 0),
                  ('text', 1, 5),
                  ('is', 1, 10),
                  ('separated', 2, 0),
                  ('by', 3, 4),
                  ('line', 4, 1),
                  ('breaks', 4, 6))]]

    @assert_equal(general_methods.get_words_from_file, iterable=True)
    @append_arguments(True)
    @wrap_string_in_io()
    def test_get_words_with_line_break(self):
        return [
            ['The quick brown-fox ju-\nmps over\n the lazy dog-',
             False, (('The', 1, 0),
                     ('quick', 1, 4),
                     ('brown', 1, 10),
                     ('fox', 1, 17),
                     ('jumps', 1, 20),
                     ('over', 2, 4),
                     ('the', 3, 1),
                     ('lazy', 3, 5),
                     ('dog', 3, 10))],
            ['The quick brown-fox ju-\nmps over\nthe lazy dog-',
             True, (('The', 1, 0),
                    ('quick', 1, 4),
                    ('brown', 1, 10),
                    ('fox', 1, 17),
                    ('jumps', 1, 20),
                    ('overthe', 2, 4),
                    ('lazy', 3, 4),
                    ('dog', 3, 9))]]


if __name__ == '__main__':
    unittest.main()
