import unittest
import requests_mock
import json
from aprsfiapi.api import API
from aprsfiapi.response import Response
from aprsfiapi.tests.support import requests


class APITest(unittest.TestCase):
    def setUp(self):
        self.aprsfiapi = API('api_key_example')

    def test_initialize_with_api_key(self):
        self.assertEqual(self.aprsfiapi._api_key, 'api_key_example')

    def test_initialize_with_string_template_for_aprs_fi_url(self):
        self.assertEqual(self.aprsfiapi._api_url, "http://api.aprs.fi/api/get?name={name}&what={what}&apikey=api_key_example&format=json")

    @requests_mock.mock()
    def test_return_basic_location_json_for_a_single_name(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA&what=loc&apikey=api_key_example&format=json',
            json=json.dumps(requests.single_name_location_success(), ensure_ascii=False))
        response  = Response(requests.single_name_location_success())
        self.assertEqual(self.aprsfiapi.loc('OH7RDA'), response)

    @requests_mock.mock()
    def test_return_basic_location_json_for_many_names(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA,OH7RDB&what=loc&apikey=api_key_example&format=json',
            json=json.dumps(requests.many_names_locations_success(), ensure_ascii=False))
        response  = Response(requests.many_names_locations_success())
        self.assertEqual(self.aprsfiapi.loc('OH7RDA', 'OH7RDB').found, 2)
        self.assertEqual(self.aprsfiapi.loc('OH7RDA', 'OH7RDB'), response)
