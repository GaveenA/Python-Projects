import unittest
from task1 import HashTable
from task2 import load_dictionary

class TestTask2(unittest.TestCase):
    def testing_task2_load_dictionary(self):


        # The objective of this test is to run load_dictionary on english_small.txt and the check if the key_value parts
        # are correct for a number of keys (words).
        # in each case the key is a differnt word and the value expected to be 1.

        hash_table = HashTable()
        load_dictionary(hash_table, 'english_small.txt')

        self.assertEqual(hash_table['disenfranchised'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['expirations'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['bewailed'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['denaturalise'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['glitter'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['guys'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['formaldehyde'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['electrodynamometer'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['jitterbugged'], 1, msg=f"The Key-Value pair is Not valid")
        self.assertEqual(hash_table['bacteriologic'], 1, msg=f"The Key-Value pair is Not valid")


if __name__ == '__main__':
  unittest.main()