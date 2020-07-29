import unittest
from task8 import HashTable

class TestTask8(unittest.TestCase):
    def test_delete(self):

        # Deleting from an empty hash table and checking if this action raises a KeyError
        hash_table = HashTable()
        with self.assertRaises(KeyError):
            hash_table.delete(2)


        #adding key - value pairs into the HashTable
        hash_table = HashTable()
        for i in range(11):
            hash_table[i] = i

        #Deleting 7 from the hashtable then trying to delete again and check if KeyError raised to ensure the element is successfully deleted
        hash_table.delete(7)
        with self.assertRaises(KeyError):
            hash_table.delete(7)

        # We are Checking if self.count is updated accordingly after deletion of element.
        self.assertEqual(hash_table.count, 10,msg="Invalid count after deletion")

        # Deleting 5 from the hashtable then trying to delete again and check if KeyError raised to ensure the element is successfully deleted
        # We also check if the count is updated accordingly

        hash_table.delete(5)
        with self.assertRaises(KeyError):
            hash_table.delete(5)
        self.assertEqual(hash_table.count, 9, msg="Invalid count after deletion")






