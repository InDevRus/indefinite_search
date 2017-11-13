import unittest
import pathmagic
from nominal_search import nominal_search as search
from tests.test_decorators import *


class NominalSearchTests(unittest.TestCase):
    @assert_equal(search, iterable=True)
    @append_arguments(False, False, False)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_nominal_search(self):
        return [['Tris is my text.',
                 ['us', 'temt', 'this', 'crouch', 'ab0'], 1,
                 ('For word "us":',
                  '    "is" in 1 line, 2 position with 1 length.',
                  '    "is" in 1 line, 5 position with 1 length.',
                  '    "s" in 1 line, 3 position with 1 length.',
                  '    "s" in 1 line, 6 position with 1 length.',
                  '    Total 4 occurrences.',
                  'For word "temt":',
                  '    "text" in 1 line, 11 position with 1 length.',
                  '    Total 1 occurrence.',
                  'For word "this":',
                  '    No occurrences found.',
                  'For word "crouch":',
                  '    No occurrences found.',
                  '"ab0" is not a word.')],
                ['Я притворяюсь, будто что-то ищу.',
                 ['бутта', 'претворяюс'], 2,
                 ('For word "бутта":',
                  '    "будто" in 1 line, 15 position with 2 length.',
                  '    "будт" in 1 line, 15 position with 2 length.',
                  '    Total 2 occurrences.',
                  'For word "претворяюс":',
                  '    "притворяюс" in 1 line, 2 position with 1 length.',
                  '    "притворяю" in 1 line, 2 position with 2 length.',
                  '    "ритворяюс" in 1 line, 3 position with 2 length.',
                  '    " притворяюс" in 1 line, 1 position with 2 length.',
                  '    "притворяюсь" in 1 line, 2 position with 2 length.',
                  '    Total 5 occurrences.')]]

    @assert_equal(search, iterable=True)
    @append_arguments(True, False, False)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_nominal_search_with_ignore_case(self):
        return [['This is my text.', ['us', 'temt', 'this', 'crouch'], 1,
                 ('For word "us":',
                  '    "is" in 1 line, 2 position with 1 length.',
                  '    "is" in 1 line, 5 position with 1 length.',
                  '    "s" in 1 line, 3 position with 1 length.',
                  '    "s" in 1 line, 6 position with 1 length.',
                  '    Total 4 occurrences.',
                  'For word "temt":',
                  '    "text" in 1 line, 11 position with 1 length.',
                  '    Total 1 occurrence.',
                  'For word "this":',
                  '    "This" in 1 line, 0 position with 0 length.',
                  '    "Thi" in 1 line, 0 position with 1 length.',
                  '    "his" in 1 line, 1 position with 1 length.',
                  '    "This " in 1 line, 0 position with 1 length.',
                  '    Total 4 occurrences.',
                  'For word "crouch":',
                  '    No occurrences found.')]]

    @assert_equal(search, iterable=True)
    @append_arguments(False, True, False)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_nominal_search_with_line_break(self):
        return [['Jived -\nf-\nox nym-\nph grabs quick walt-\nz.',
                 ['pox', 'walts'], 1,
                 ('For word "pox":',
                  '    "fox" in 2 line, 0 position with 1 length.',
                  '    "ox" in 3 line, 0 position with 1 length.',
                  '    Total 2 occurrences.',
                  'For word "walts":',
                  '    "waltz" in 4 line, 15 position with 1 length.',
                  '    "walt" in 4 line, 15 position with 1 length.',
                  '    Total 2 occurrences.')]]

    @assert_equal(search, iterable=True)
    @append_arguments(False, False, True)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_sort_output(self):
     return [['Tris is my text.',
              ['temt', ], 8,
              ('For word "temt":',
               '    "text" in 1 line, 11 position with 1 length.',
               '    "tex" in 1 line, 11 position with 2 length.',
               '    "ext" in 1 line, 12 position with 2 length.',
               '    " text" in 1 line, 10 position with 2 length.',
               '    "text." in 1 line, 11 position with 2 length.',
               '    "te" in 1 line, 11 position with 2 length.',
               '    "s my" in 1 line, 6 position with 3 length.',
               '    "my t" in 1 line, 8 position with 3 length.',
               '    " tex" in 1 line, 10 position with 3 length.',
               '    "ext." in 1 line, 12 position with 3 length.',
               '    "s m" in 1 line, 6 position with 3 length.',
               '    " my" in 1 line, 7 position with 3 length.',
               '    "y t" in 1 line, 9 position with 3 length.',
               '    " te" in 1 line, 10 position with 3 length.',
               '    " m" in 1 line, 7 position with 3 length.',
               '    "my" in 1 line, 8 position with 3 length.',
               '    " t" in 1 line, 10 position with 3 length.',
               '    "ex" in 1 line, 12 position with 3 length.',
               '    "xt" in 1 line, 13 position with 3 length.',
               '    "t." in 1 line, 14 position with 3 length.',
               '    "y text" in 1 line, 9 position with 3 length.',
               '    " text." in 1 line, 10 position with 3 length.',
               '    "m" in 1 line, 8 position with 3 length.',
               '    "t" in 1 line, 11 position with 3 length.',
               '    "e" in 1 line, 12 position with 3 length.',
               '    "t" in 1 line, 14 position with 3 length.',
               '    "Tris" in 1 line, 0 position with 4 length.',
               '    "ris " in 1 line, 1 position with 4 length.',
               '    "is i" in 1 line, 2 position with 4 length.',
               '    "s is" in 1 line, 3 position with 4 length.',
               '    " is " in 1 line, 4 position with 4 length.',
               '    "is m" in 1 line, 5 position with 4 length.',
               '    " my " in 1 line, 7 position with 4 length.',
               '    "y te" in 1 line, 9 position with 4 length.',
               '    "Tri" in 1 line, 0 position with 4 length.',
               '    "ris" in 1 line, 1 position with 4 length.',
               '    "is " in 1 line, 2 position with 4 length.',
               '    "s i" in 1 line, 3 position with 4 length.',
               '    " is" in 1 line, 4 position with 4 length.',
               '    "is " in 1 line, 5 position with 4 length.',
               '    "my " in 1 line, 8 position with 4 length.',
               '    "xt." in 1 line, 13 position with 4 length.',
               '    "is my" in 1 line, 5 position with 4 length.',
               '    "s my " in 1 line, 6 position with 4 length.',
               '    " my t" in 1 line, 7 position with 4 length.',
               '    "my te" in 1 line, 8 position with 4 length.',
               '    "y tex" in 1 line, 9 position with 4 length.',
               '    "Tr" in 1 line, 0 position with 4 length.',
               '    "ri" in 1 line, 1 position with 4 length.',
               '    "is" in 1 line, 2 position with 4 length.',
               '    "s " in 1 line, 3 position with 4 length.',
               '    " i" in 1 line, 4 position with 4 length.',
               '    "is" in 1 line, 5 position with 4 length.',
               '    "s " in 1 line, 6 position with 4 length.',
               '    "y " in 1 line, 9 position with 4 length.',
               '    "s my t" in 1 line, 6 position with 4 length.',
               '    "T" in 1 line, 0 position with 4 length.',
               '    "r" in 1 line, 1 position with 4 length.',
               '    "i" in 1 line, 2 position with 4 length.',
               '    "s" in 1 line, 3 position with 4 length.',
               '    " " in 1 line, 4 position with 4 length.',
               '    "i" in 1 line, 5 position with 4 length.',
               '    "s" in 1 line, 6 position with 4 length.',
               '    " " in 1 line, 7 position with 4 length.',
               '    "y" in 1 line, 9 position with 4 length.',
               '    " " in 1 line, 10 position with 4 length.',
               '    "x" in 1 line, 13 position with 4 length.',
               '    "." in 1 line, 15 position with 4 length.',
               '    "my text" in 1 line, 8 position with 4 length.',
               '    "y text." in 1 line, 9 position with 4 length.',
               '    "Tris " in 1 line, 0 position with 5 length.',
               '    "ris i" in 1 line, 1 position with 5 length.',
               '    "is is" in 1 line, 2 position with 5 length.',
               '    "s is " in 1 line, 3 position with 5 length.',
               '    " is m" in 1 line, 4 position with 5 length.',
               '    " is my" in 1 line, 4 position with 5 length.',
               '    "is my " in 1 line, 5 position with 5 length.',
               '    " my te" in 1 line, 7 position with 5 length.',
               '    "my tex" in 1 line, 8 position with 5 length.',
               '    "is my t" in 1 line, 5 position with 5 length.',
               '    "s my te" in 1 line, 6 position with 5 length.',
               '    " my text" in 1 line, 7 position with 5 length.',
               '    "my text." in 1 line, 8 position with 5 length.',
               '    "Tris i" in 1 line, 0 position with 6 length.',
               '    "ris is" in 1 line, 1 position with 6 length.',
               '    "is is " in 1 line, 2 position with 6 length.',
               '    "s is m" in 1 line, 3 position with 6 length.',
               '    "s is my" in 1 line, 3 position with 6 length.',
               '    " is my " in 1 line, 4 position with 6 length.',
               '    " my tex" in 1 line, 7 position with 6 length.',
               '    " is my t" in 1 line, 4 position with 6 length.',
               '    "is my te" in 1 line, 5 position with 6 length.',
               '    "s my tex" in 1 line, 6 position with 6 length.',
               '    "s my text" in 1 line, 6 position with 6 length.',
               '    " my text." in 1 line, 7 position with 6 length.',
               '    "Tris is" in 1 line, 0 position with 7 length.',
               '    "ris is " in 1 line, 1 position with 7 length.',
               '    "is is m" in 1 line, 2 position with 7 length.',
               '    "is is my" in 1 line, 2 position with 7 length.',
               '    "s is my " in 1 line, 3 position with 7 length.',
               '    "s is my t" in 1 line, 3 position with 7 length.',
               '    " is my te" in 1 line, 4 position with 7 length.',
               '    "is my tex" in 1 line, 5 position with 7 length.',
               '    "is my text" in 1 line, 5 position with 7 length.',
               '    "s my text." in 1 line, 6 position with 7 length.',
               '    "Tris is " in 1 line, 0 position with 8 length.',
               '    "ris is m" in 1 line, 1 position with 8 length.',
               '    "ris is my" in 1 line, 1 position with 8 length.',
               '    "is is my " in 1 line, 2 position with 8 length.',
               '    "is is my t" in 1 line, 2 position with 8 length.',
               '    "s is my te" in 1 line, 3 position with 8 length.',
               '    " is my tex" in 1 line, 4 position with 8 length.',
               '    " is my text" in 1 line, 4 position with 8 length.',
               '    "is my text." in 1 line, 5 position with 8 length.',
               '    Total 114 occurrences.')],
             ['Я притворяюсь, будто что-то ищу.',
              ['бутта', ], 3,
              ('For word "бутта":',
               '    "будто" in 1 line, 15 position with 2 length.',
               '    "будт" in 1 line, 15 position with 2 length.',
               '    " будт" in 1 line, 14 position with 3 length.',
               '    "удто" in 1 line, 16 position with 3 length.',
               '    " будто" in 1 line, 14 position with 3 length.',
               '    "будто " in 1 line, 15 position with 3 length.',
               '    "буд" in 1 line, 15 position with 3 length.',
               '    "удт" in 1 line, 16 position with 3 length.',
               '    "бу" in 1 line, 15 position with 3 length.',
               '    Total 9 occurrences.')]]


if __name__ == '__main__':
    unittest.main()
