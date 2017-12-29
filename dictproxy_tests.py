import unittest
import dictproxy

class DictproxyTestCase(unittest.TestCase):

    def setUp(self):
        dictproxy.app.testing = True
        self.app = dictproxy.dictproxy.app.test_client()

    def test_hello_world(self):
        result = self.app.get('/')
        assert b'Hello, World!' in result.data

if __name__ == '__main__':
    unittest.main()
