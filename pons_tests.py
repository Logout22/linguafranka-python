import unittest
from dicts import Pons


class TestPons(unittest.TestCase):
    def test_lookup_exists(self):
        pons = Pons()
        pons.lookup('')

if __name__ == '__main__':
    unittest.main()
