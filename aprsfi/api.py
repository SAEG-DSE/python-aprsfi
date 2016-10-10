import json
import requests
from aprsfi.response import Response


class RequestException(Exception):
    pass


class API(object):

    def __init__(self, api_key):
        self._api_key = api_key
        self._api_url = ("http://api.aprs.fi/api/get?name={name}&what={what}&"
                         "apikey=%s&format=json" % api_key)

    def __getattr__(self, attr):
        if attr in ['loc', 'wx']:
            def request(*args):
                url = self._api_url.format(name=','.join(args), what=attr)
                response = requests.get(url)
                response_json = response.json()
                if response_json['result'] == 'fail':
                    raise RequestException(
                        response_json['description'])
                return Response(response_json)
            return request
        else:
            raise AttributeError
