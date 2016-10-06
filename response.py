from aprsfiapi.entry import Entry

class Response(object):

    def __init__(self, response_dict):
        request_entries = response_dict.pop('entries', None)
        if request_entries:
            self.entries = [Entry(entry) for entry in request_entries]
        self._data = response_dict

    def __getattr__(self, attr):
        if attr in self._data:
            return self._data[attr]
        else:
            raise AttributeError
