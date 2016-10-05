import unittest
from aprsfiapi.entry import Entry


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


if __name__ == '__main__':
    unittest.main()
