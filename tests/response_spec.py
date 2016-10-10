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

    def test_return_true_if_quantity_and_names_is_equal(self):
        first_response  = Response(requests.single_name_location_success())
        second_response = Response(requests.single_name_location_success())
        self.assertTrue(first_response == second_response)

    def test_return_false_if_quantity_and_names_is_not_equal(self):
        first_response  = Response(requests.single_name_location_success())
        second_response = Response(requests.another_single_name_location_success())
        self.assertFalse(first_response == second_response)

    def test_return_attribute_error_for_nonexistent_field(self):
        response = Response(requests.single_name_location_success())
        with self.assertRaises(AttributeError):
            response.nonexistent_field
