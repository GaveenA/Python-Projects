import unittest
from task1 import HashTable

class TestTask1(unittest.TestCase):

    def test_set_item(self):

        # Testing SetItem whe array is full
        hash_table = HashTable()
        for i in range(11):
            hash_table.insert(f"{i}", i)
        hash_table[10] = 'Hello'  # Hash of key = 10 is 3 (after probing) (default tablesize = 11, hashbase = 31)
        self.assertEqual(hash_table.array[3][1], 'Hello', msg=f"Set-Item has failed")
        hash_table[9] = 'Hello2' # Hash of key = 9 is 2 (default tablesize = 11, hashbase = 31)
        self.assertEqual(hash_table.array[2][1], 'Hello2', msg=f"Set-Item has failed")

        hash_table = HashTable()
        hash_table['Gaveen'] = 'First Name'      # Hash of 'gaveen' == 1 (default tablesize = 11, hashbase = 31)
        hash_table['Amarapala'] = 'Surname'      #  Hash of 'amarapala' == 2 (default tablesize = 11, hashbase = 31)
        hash_table[1] = '1'                      #  Hash of '1' == 5 (default tablesize = 11, hashbase = 31)

        self.assertEqual(hash_table.array[1][1], 'First Name', msg=f"Set-Item has failed") # Assertion to check if insert has worked
        self.assertEqual(hash_table.array[2][1], 'Surname', msg=f"Set-Item has failed")  # Assertion to check if insert has worked
        self.assertEqual(hash_table.array[5][1], '1',msg=f"Set-Item has failed")  # Assertion to check if insert has worked




    def test_rehash(self):
        # Test to check if rehash changes the size of HashTable to the prime larger than 2 x self.capacity
        hash_table = HashTable()
        for i in range(11):
            hash_table.insert(f"{i}",1)
        hash_table.insert(12, 12)
        self.assertEqual(len(hash_table.array), 23, msg = 'Size of HashTable has not increased to the prime larger than 2 x self.capacity')

        # Test to check if rehash changes the size of HashTable to the prime larger than 2 x self.capacity
        hash_table = HashTable()
        for i in range(12):
            hash_table.insert(f"{i}", 1)
        self.assertEqual(len(hash_table.array), 23, msg="Size of HashTable has not increased to the prime larger than 2 x self.capacity")

        # Test to check that updating the last value in hashTable does not increase the tableSize
        hash_table = HashTable()
        for i in range(11):
            hash_table.insert(f"{i}",1)
        hash_table[10] = 'Test'
        self.assertEqual(len(hash_table.array), 11, msg='Size of HashTable should remain')



if __name__ == '__main__':
    unittest.main()




