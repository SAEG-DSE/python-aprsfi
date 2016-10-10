from aprsfi.entry import Entry


class Response(object):

    def __init__(self, response_dict):
        request_entries = response_dict.pop('entries', None)
        if request_entries:
            self.entries = [Entry(entry) for entry in request_entries]
        self._data = response_dict

    def __eq__(self, another_response):
        self_response_names = list(map(lambda e: e.name, self.entries))
        self_response_names.sort()
        another_response_names = list(map(lambda e: e.name,
                                          another_response.entries))
        another_response_names.sort()
        return (self._data == another_response._data and
                self_response_names == another_response_names)

    def __getattr__(self, attr):
        if attr in self._data:
            return self._data[attr]
        else:
            raise AttributeError
