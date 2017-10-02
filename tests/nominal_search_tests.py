import unittest
import pathmagic
from nominal_search import nominal_search as search
from tests.test_decorators import assert_function,\
    wrap_string_in_io, append_arguments, wrap_list_in_io


class NominalSearchTests(unittest.TestCase):
    @assert_function(search, iterable=True)
    @append_arguments(False, False)
    @wrap_list_in_io()
    @wrap_string_in_io()
    def test_nominal_search(self):
        return [['Tris is my text.',
                 ['us', 'temt', 'this', 'crouch', 'ab0'], 1,
                 ('For word "us":',
                  '    "is" in 1 line, 2 position.',
                  '    "is" in 1 line, 5 position.',
                  '    "s" in 1 line, 3 position.',
                  '    "s" in 1 line, 6 position.',
                  '    Total 4 occurrences.',
                  '',
                  'For word "temt":',
                  '    "text" in 1 line, 11 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "this":',
                  '    No occurrences found.',
                  '',
                  'For word "crouch":',
                  '    No occurrences found.',
                  '',
                  '"ab0" is not a word.')],
                ['Я притворяюсь, будто что-то ищу.',
                 ['бутта', 'претворяюс'], 2,
                 ('For word "бутта":',
                  '    "будто" in 1 line, 15 position.',
                  '    "будт" in 1 line, 15 position.',
                  '    Total 2 occurrences.',
                  '',
                  'For word "претворяюс":',
                  '    "притворяюс" in 1 line, 2 position.',
                  '    "притворяю" in 1 line, 2 position.',
                  '    "ритворяюс" in 1 line, 3 position.',
                  '    " притворяюс" in 1 line, 1 position.',
                  '    "притворяюсь" in 1 line, 2 position.',
                  '    Total 5 occurrences.')]]

    @assert_function(search, iterable=True)
    @append_arguments(True, False)
    @wrap_list_in_io()
    @wrap_string_in_io()
    def test_nominal_search_with_ignore_case(self):
        return [['This is my text.', ['us', 'temt', 'this', 'crouch'], 1,
                 ('For word "us":',
                  '    "is" in 1 line, 2 position.',
                  '    "is" in 1 line, 5 position.',
                  '    "s" in 1 line, 3 position.',
                  '    "s" in 1 line, 6 position.',
                  '    Total 4 occurrences.',
                  '',
                  'For word "temt":',
                  '    "text" in 1 line, 11 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "this":',
                  '    "This" in 1 line, 0 position.',
                  '    "Thi" in 1 line, 0 position.',
                  '    "his" in 1 line, 1 position.',
                  '    "This " in 1 line, 0 position.',
                  '    Total 4 occurrences.',
                  '',
                  'For word "crouch":',
                  '    No occurrences found.')]]

    @assert_function(search, iterable=True)
    @append_arguments(False, True)
    @wrap_list_in_io()
    @wrap_string_in_io()
    def test_nominal_search_with_line_break(self):
        return [['Jived -\nf-\nox nym-\nph grabs quick walt-\nz.',
                 ['pox', 'walts'], 1,
                 ('For word "pox":',
                  '    "fox" in 2 line, 0 position.',
                  '    "ox" in 3 line, 0 position.',
                  '    Total 2 occurrences.',
                  '',
                  'For word "walts":',
                  '    "waltz" in 4 line, 15 position.',
                  '    "walt" in 4 line, 15 position.',
                  '    Total 2 occurrences.')]]


if __name__ == '__main__':
    unittest.main()
