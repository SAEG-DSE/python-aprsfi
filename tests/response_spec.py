import unittest
from aprsfiapi.response import Response
from aprsfiapi.tests.support import requests
from aprsfiapi.entry import Entry


class ResponseTest(unittest.TestCase):

    def test_initialize_with_a_hash(self):
        response = Response(requests.single_name_location_success())
        self.assertEqual(response._data, {"command":"get", "result":"ok",
    	"what":"loc", "found":1})

    def test_create_dynamically_attributes(self):
        response = Response(requests.single_name_location_success())
        self.assertEqual(response.command, 'get')
        self.assertEqual(response.result, 'ok')
        self.assertEqual(response.what, 'loc')
        self.assertEqual(response.found, 1)

    def test_create_entries_on_initialize(self):
        entry = Entry(requests.single_name_location_success()["entries"][0])
        response = Response(requests.single_name_location_success())
        self.assertEqual(response.entries, [entry])

    def test_also_create_entries_on_initialize_for_many_names(self):
        entries = [Entry(entry) for entry in requests.many_names_locations_success()["entries"]]
        response = Response(requests.many_names_locations_success())
        self.assertEqual(response.entries, entries)
