from .pons_parser import PonsParser

class Pons(object):
    def __init__(self, data_source):
        self.data_source = data_source
        self.parser = PonsParser()

    def lookup(self, word):
        if not self.data_source:
            return ''

        query_result = self.data_source.query_word(word)
        self.parser.feed(query_result)
        result = self.parser.lookup_table
        return result
