from django.test import TestCase
from paste.utils import short_hash

class UtilsTest(TestCase):

    def test_short_hash_returns_8_characters(self):
        test_hash = short_hash()
        self.assertEqual(len(test_hash), 8)

    def test_short_hash_generates_unique_hashes(self):
        hashes = set([short_hash() for _ in range(10)])
        self.assertEqual(len(hashes), 10)

