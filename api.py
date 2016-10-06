import string


class API(object):

    def __init__(self, api_key):
        self._api_key = api_key
        self._api_url = "http://api.aprs.fi/api/get?name={name}&what={what}&apikey=%s&format=json" % api_key
