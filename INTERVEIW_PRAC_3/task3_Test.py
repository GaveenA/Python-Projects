import unittest
from task3 import*

class TestTask3(unittest.TestCase):
    def test_setItem(self):

        hash_table = HashTable(3, 31)
        # Keys 0, 3, 6, will hash to position 0 with table size = 3.
        for i in [0, 3, 6]:
            hash_table[i] = i
        stats = hash_table.statistics()
        self.assertEqual(stats[0], 2,msg=f"Error in Calculation of Collision Count")
        self.assertEqual(stats[1], 3,msg=f"Error in Calculation of Probe Total")
        self.assertEqual(stats[2], 2,msg=f"Error in Calculation of Probe Max")
        self.assertEqual(stats[3], 0,msg=f"Error in Calculation of Rehash Count")

        # After insertion of one new key onto the HashTable - k, the table size will now increase to 7
        # and the new hash values of:
        # 0 is 6
        # 3 is 2
        # 6 is 5

        # we will now insert 4 new keys = 1, 8, 11, 18 respectively
        # and they all hash to 0 when tableSize = 7, therefore after the first new key (1) occupies position 0
        # each corresponding key inserted will experience a collision.
        hash_table.insert(1, 1)
        hash_table.insert(8, 8)
        hash_table.insert(11, 11)
        hash_table.insert(18, 18)
        stats2 = hash_table.statistics()

        self.assertEqual(stats2[0], 5, msg=f"Error in Calculation of Collision Count")
        self.assertEqual(stats2[1], 11, msg=f"Error in Calculation of Probe Total")
        self.assertEqual(stats2[2], 4, msg=f"Error in Calculation of Probe Max")
        self.assertEqual(stats2[3], 1, msg=f"Error in Calculation of Rehash Count")


if __name__ == '__main__':
  unittest.main()
