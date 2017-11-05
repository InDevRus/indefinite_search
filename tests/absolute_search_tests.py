import unittest
import pathmagic
from tests.test_decorators import assert_equal, \
    append_arguments, wrap_string_in_io
from absolute_search import absolute_search as search


class AbsoluteSearchTests(unittest.TestCase):
    @assert_equal(search, iterable=True)
    @append_arguments(False, False, False)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_absolute_search(self):
        return [['Tris is\nmy text.', ['my', 'ma', 'temt', 'This', 'ab0'], 1,
                 ('For word "my":',
                  '    "my" in 2 line, 0 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "ma":',
                  '    "my" in 2 line, 0 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "temt":',
                  '    "text" in 2 line, 3 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "This":',
                  '    "Tris" in 1 line, 0 position.',
                  '    Total 1 occurrence.',
                  '',
                  '"ab0" is not a word.')]]

    @assert_equal(search, iterable=True)
    @append_arguments(False, True, False)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_absolute_search_with_ignore_case(self):
        return [['This is my text with SPACES.',
                 ['us', 'temt', 'this', 'crouch', 'spAce'],
                 1,
                 ('For word "us":',
                  '    "is" in 1 line, 5 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "temt":',
                  '    "text" in 1 line, 11 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "this":',
                  '    "This" in 1 line, 0 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "crouch":',
                  '    No occurrences found.',
                  '',
                  'For word "spAce":',
                  '    "SPACES" in 1 line, 21 position.',
                  '    Total 1 occurrence.')]]

    @assert_equal(search, iterable=True)
    @append_arguments(True, False, True)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_absolute_search_with_line_break(self):
        return [['Jived -\nf-\nox nym-\nph grabs quick walt-\nz.',
                 ['pox', 'walts'], 1,
                 ('For word "pox":',
                  '    "fox" in 1 line, 6 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "walts":',
                  '    "waltz" in 4 line, 15 position.',
                  '    Total 1 occurrence.')]]

    @assert_equal(search, iterable=True)
    @append_arguments(True, False, False)
    @wrap_string_in_io(1, iterable=True)
    @wrap_string_in_io()
    def test_absolute_search_without_word_wrap(self):
        return [['Glib jocks qu\niz nymph \nto ve\nx dwa-\nrf.',
                 ['Glib', 'quis', 'to', 'veh', 'dwarf'], 1,
                 ('For word "Glib":',
                  '    "Glib" in 1 line, 0 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "quis":',
                  '    "quiz" in 1 line, 11 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "to":',
                  '    "to" in 3 line, 0 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "veh":',
                  '    "vex" in 3 line, 3 position.',
                  '    Total 1 occurrence.',
                  '',
                  'For word "dwarf":',
                  '    No occurrences found.')]]


if __name__ == '__main__':
    unittest.main()
