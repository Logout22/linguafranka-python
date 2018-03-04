import unittest
from dicts import Dicts


class ExampleTable1:
    SPAM_TRANS = ['SPAM', 'SPAM' 'SPAM']
    BREAKFAST_TRANS = ['egg', 'bacon', 'spam']

    def lookup(self, word):
        if word == 'spam':
            return self.SPAM_TRANS
        elif word == 'breakfast':
            return self.BREAKFAST_TRANS


class ExampleTable2:
    SPAM_TRANS = ['SPAMO', 'SPAMI' 'SPAMA']
    BREAKFAST_TRANS = ['egge', 'baco', 'span']

    def lookup(self, word):
        if word == 'spam':
            return self.SPAM_TRANS
        elif word == 'breakfast':
            return self.BREAKFAST_TRANS


class TestDicts(unittest.TestCase):
    def test_lookup_exists(self):
        dicts = Dicts(None)
        dicts.lookup('')

    def test_lookup_returns_word_unchanged_without_tables(self):
        dicts = Dicts(None)
        self.assertEqual(['gnarble'], dicts.lookup('gnarble'))

    def test_return_expected_translation(self):
        dicts = Dicts([ExampleTable1()])
        self.assertEqual([ExampleTable1.SPAM_TRANS], dicts.lookup('spam'))
        self.assertEqual([ExampleTable1.BREAKFAST_TRANS], dicts.lookup('breakfast'))

    def test_return_translations_from_multiple_tables(self):
        dicts = Dicts([ExampleTable1(), ExampleTable2()])
        self.assertEqual(
                [ExampleTable1.SPAM_TRANS, ExampleTable2.SPAM_TRANS],
                dicts.lookup('spam'))
        self.assertEqual(
                [ExampleTable1.BREAKFAST_TRANS, ExampleTable2.BREAKFAST_TRANS],
                dicts.lookup('breakfast'))

if __name__ == '__main__':
    unittest.main()
