import unittest
from dicts import Pons


class IntegrationTestDataSource(object):
    def query_word(self, _):
        return open('examples/pons.html').read()


class TestPons(unittest.TestCase):
    def test_lookup_exists(self):
        pons = Pons(None)
        pons.lookup('')

    def test_integration_whole_file(self):
        pons = Pons(IntegrationTestDataSource())
        result = pons.lookup('test')
        self.assertEqual([], result)


if __name__ == '__main__':
    unittest.main()
