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


if __name__ == '__main__':
    unittest.main()
