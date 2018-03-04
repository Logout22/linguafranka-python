class Dicts:
    def __init__(self, active_tables):
        self._active_tables = active_tables

    def lookup(self, word):
        return [active_table.lookup(word) for active_table in self._active_tables] \
                if self._active_tables \
                else [word]
