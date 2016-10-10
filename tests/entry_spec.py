import unittest
from aprsfi.entry import Entry


class EntryTest(unittest.TestCase):

    def setUp(self):
        self.entry = Entry({'name': 'OH7RDA', 'type': 'l'})

    def test_initialize_with_dict(self):
        self.assertEqual(self.entry._data, {'name': 'OH7RDA', 'type': 'l'})

    def test_create_dynamically_attributes(self):
        self.assertEqual(self.entry.name, 'OH7RDA')
        self.assertEqual(self.entry.type, 'l')

    def test_return_all_attributes(self):
        fields = self.entry.fields
        fields.sort()
        self.assertEqual(fields, ['name', 'type'])

    def test_return_attribute_error_for_nonexistent_field(self):
        with self.assertRaises(AttributeError):
            self.entry.nonexistent_field

    def test_return_equal_if_data_is_equal(self):
        first_entry = Entry({'name': 'OH7RDA', 'type': 'l'})
        second_entry = Entry({'name': 'OH7RDA', 'type': 'l'})
        self.assertTrue(first_entry == second_entry)

    def test_return_not_equal_if_data_is_not_equal(self):
        first_entry = Entry({'name': 'OH7RDB', 'type': 'l'})
        second_entry = Entry({'name': 'OH7RDA', 'type': 'l'})
        self.assertFalse(first_entry == second_entry)


if __name__ == '__main__':
    unittest.main()
