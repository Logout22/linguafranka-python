import unittest
from dicts import Pons


TEST_WORD = 'test'


class IntegrationTestDataSource(object):
    def query_word(self, word):
        if word != TEST_WORD:
            return ''
        return open('examples/pons.html').read()


class TestPons(unittest.TestCase):
    def test_lookup_exists(self):
        pons = Pons(None)
        pons.lookup('')

    def test_integration_whole_file(self):
        pons = Pons(IntegrationTestDataSource())
        result = pons.lookup(TEST_WORD)
        self.assertEqual([], result)


if __name__ == '__main__':
    unittest.main()
