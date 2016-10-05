class Entry(object):

    def __init__(self, data):
        self._data = data

    @property
    def fields(self):
        return self._data.keys()


    def __getattr__(self, attr):
        if self._data.has_key(attr):
            return self._data[attr]
        else:
            raise AttributeError
