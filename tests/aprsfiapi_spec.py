import unittest
from aprsfiapi.api import API


class APITest(unittest.TestCase):
    def setUp(self):
        self.aprsfiapi = API('api_key_example')

    def test_initialize_with_api_key(self):
        self.assertEqual(self.aprsfiapi._api_key, 'api_key_example')

    def test_initialize_with_string_template_for_aprs_fi_url(self):
        self.assertEqual(self.aprsfiapi._api_url, "http://api.aprs.fi/api/get?name={name}&what={what}&apikey=api_key_example&format=json")
