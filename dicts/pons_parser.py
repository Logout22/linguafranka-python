import unittest
from enum import Enum
from html.parser import HTMLParser

class TestPonsParser(unittest.TestCase):
    def test_find_translation(self):
        tag_string = """
<dl>
<dt>
pregnancy test
</dt>
<dd>
Schwangerschaftstest
</dd>
</dl>
        """
        tags = {"pregnancy test": ["Schwangerschaftstest"]}
        pons_parser = PonsParser()
        pons_parser.feed(tag_string)
        self.assertEqual(tags, pons_parser.lookup_table)

class PonsParserStates(Enum):
    SEARCHING = 0
    IN_DT = 1
    IN_DD = 2

class PonsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.state = PonsParserStates.SEARCHING
        self.current_key = ""
        self.lookup_table = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'dt':
            self.state = PonsParserStates.IN_DT
        elif tag == 'dd':
            self.state = PonsParserStates.IN_DD

    def handle_endtag(self, tag):
        self.state = PonsParserStates.SEARCHING

    def handle_data(self, data):
        if self.state == PonsParserStates.IN_DT:
            self.current_key = data.strip()
        elif self.state == PonsParserStates.IN_DD:
            self.append_to_lookup_table(data)

    def append_to_lookup_table(self, data):
        if self.current_key not in self.lookup_table:
            self.lookup_table[self.current_key] = []
        self.lookup_table[self.current_key].append(data.strip())


if __name__ == '__main__':
    unittest.main()
