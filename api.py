import json
import requests
from aprsfiapi.response import Response


class RequestException(Exception):
    pass


class API(object):

    def __init__(self, api_key):
        self._api_key = api_key
        self._api_url = ("http://api.aprs.fi/api/get?name={name}&what={what}&"
                         "apikey=%s&format=json" % api_key)

    def loc(self, *args):
        url = self._api_url.format(name=','.join(args), what='loc')
        response = requests.get(url)
        if json.loads(response.json())['result'] == 'fail':
            raise RequestException(json.loads(response.json())['description'])
        return Response(json.loads(response.json()))

    def wx(self, *args):
        url = self._api_url.format(name=','.join(args), what='wx')
        response = requests.get(url)
        if json.loads(response.json())['result'] == 'fail':
            raise RequestException(json.loads(response.json())['description'])
        return Response(json.loads(response.json()))
