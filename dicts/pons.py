from .pons_parser import PonsParser

class Pons(object):
    def __init__(self, data_source):
        self.data_source = data_source
        self.parser = PonsParser()

    def lookup(self, word):
        pass
