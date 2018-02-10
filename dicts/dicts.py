class Dicts:
    def __init__(self, active_table):
        self._active_table = active_table

    def lookup(self, word):
        return self._active_table.lookup(word) \
                if self._active_table \
                else word
