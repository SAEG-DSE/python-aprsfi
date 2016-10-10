class Entry(object):

    def __init__(self, data):
        self._data = data

    @property
    def fields(self):
        return list(self._data)

    def __eq__(self, another_entry):
        return self._data == another_entry._data

    def __getattr__(self, attr):
        if attr in self._data:
            return self._data[attr]
        else:
            raise AttributeError
