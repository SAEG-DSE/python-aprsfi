class Entry(object):

    def __init__(self, data):
        self._data = data

    def __getattr__(self, attr):
        return self._data[attr]

    @property
    def fields(self):
        return self._data.keys()
