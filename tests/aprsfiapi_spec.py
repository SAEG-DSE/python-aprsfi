import unittest
import requests_mock
import json
from aprsfi.api import API
from aprsfi.api import RequestException
from aprsfi.response import Response
from .support import requests


class APITest(unittest.TestCase):
    def setUp(self):
        self.aprsfi = API('api_key_example')

    def test_initialize_with_api_key(self):
        self.assertEqual(self.aprsfi._api_key, 'api_key_example')

    def test_initialize_with_string_template_for_aprs_fi_url(self):
        self.assertEqual(self.aprsfi._api_url, "http://api.aprs.fi/api/get?name={name}&what={what}&apikey=api_key_example&format=json")

    @requests_mock.mock()
    def test_return_basic_location_json_for_a_single_name(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA&what=loc&apikey=api_key_example&format=json',
            json=requests.single_name_location_success())
        response = Response(requests.single_name_location_success())
        self.assertEqual(self.aprsfi.loc('OH7RDA'), response)

    @requests_mock.mock()
    def test_return_basic_location_json_for_many_names(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA,OH7RDB&what=loc&apikey=api_key_example&format=json',
            json=requests.many_names_locations_success())
        response = Response(requests.many_names_locations_success())
        self.assertEqual(self.aprsfi.loc('OH7RDA', 'OH7RDB').found, 2)
        self.assertEqual(self.aprsfi.loc('OH7RDA', 'OH7RDB'), response)

    @requests_mock.mock()
    def test_return_request_error(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA&what=loc&apikey=api_key_example&format=json',
            json=requests.fail_request())
        with self.assertRaisesRegexp(RequestException, "authentication failed: wrong API key"):
            self.aprsfi.loc('OH7RDA')

    @requests_mock.mock()
    def test_return_basic_wx_json_for_a_single_name(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA&what=loc&apikey=api_key_example&format=json',
            json=requests.single_name_wx_success())
        response = Response(requests.single_name_wx_success())
        self.assertEqual(self.aprsfi.loc('OH7RDA'), response)

    @requests_mock.mock()
    def test_return_basic_wx_json_for_many_names(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA,OH7RDB&what=loc&apikey=api_key_example&format=json',
            json=requests.many_names_wxs_success())
        response = Response(requests.many_names_wxs_success())
        self.assertEqual(self.aprsfi.loc('OH7RDA', 'OH7RDB').found, 2)
        self.assertEqual(self.aprsfi.loc('OH7RDA', 'OH7RDB'), response)

    @requests_mock.mock()
    def test_return_request_error(self, m):
        m.get('http://api.aprs.fi/api/get?name=OH7RDA&what=loc&apikey=api_key_example&format=json',
            json=requests.fail_request())
        with self.assertRaisesRegexp(RequestException, "authentication failed: wrong API key"):
            self.aprsfi.loc('OH7RDA')

    def test_return_attribute_error_for_nonexistent_field(self):
        with self.assertRaises(AttributeError):
            self.aprsfi.nonexistent_field
