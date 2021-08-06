import unittest

from src.hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def test_hash_func(self):
        """
        Check if value returned by hash function is lower than hashtable
         capacity
        """
        capacity = 5
        hash_table = HashTable(capacity=capacity)
        h = hash_table.hash_func('a')
        self.assertTrue(h < capacity)

    def test_search_simple(self):
        """
        Check if search returns None for non-existing key
        """
        hash_table = HashTable(capacity=5)
        answer = hash_table.search('a')
        self.assertIsNone(answer)

    def test_insert_simple(self):
        """
        Check if after inserting value is present in hashtable
        """
        hash_table = HashTable(capacity=5)
        hash_table.insert('a', 0)
        answer = hash_table.search('a')
        self.assertEqual(answer, 0)

    def test_delete_simple(self):
        """
        Check if after deleting value is not present in hashtable
        """
        hash_table = HashTable(capacity=5)
        hash_table.insert('a', 0)
        hash_table.delete('a')
        answer = hash_table.search('a')
        self.assertIsNone(answer)

    def test_insert_two_with_same_hash(self):
        """
        Check if after inserting two values with the same hash for keys both of
         them are present in hashtabel
        """
        hash_table = HashTable(capacity=5)
        hash_table.insert('a', 0)
        hash_table.insert('f', 1)
        answer = hash_table.search('a')
        answer2 = hash_table.search('f')
        self.assertEqual(answer, 0)
        self.assertEqual(answer2, 1)

    def test_delete_two_with_same_hash(self):
        """
        Inserting two values with same hash for keys, deleting first one of
         them, checking if it's deleted and second one is still present
        """
        hash_table = HashTable(capacity=5)
        hash_table.insert('a', 0)
        hash_table.insert('f', 1)
        hash_table.delete('a')
        answer = hash_table.search('a')
        answer2 = hash_table.search('f')
        self.assertIsNone(answer)
        self.assertEqual(answer2, 1)

    def test_delete_two_with_same_hash_2(self):
        """
        Inserting two values with same hash for keys, deleting second of
         them, checking if it's deleted and first one is still present
        """
        hash_table = HashTable(capacity=5)
        hash_table.insert('a', 0)
        hash_table.insert('f', 1)
        hash_table.delete('f')
        answer = hash_table.search('a')
        answer2 = hash_table.search('f')
        self.assertEqual(answer, 0)
        self.assertIsNone(answer2)
