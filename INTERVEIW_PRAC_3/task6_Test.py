import unittest
from task6 import Freq

class TestTask6(unittest.TestCase):

    def test_addFile(self):

        # In this Test we are considering file - testfile_task6.txt     which contains strings:
        # "a" : 1500 occurrences
        # "b" : 600 occurrences
        # "c" : 200 occurrences
        # "d" : 1 occurrence
        # "e" : 10 occurrences
        # "z" : 0 occurrences

        f = Freq()  # Creating instance of class frequency
        f.add_file("testfile_task6.txt")

        self.assertEqual(f.hash_table["a"], 1500,msg="count for 'a' incorrect ")
        self.assertEqual(f.hash_table["b"], 600, msg="count for 'b' incorrect ")
        self.assertEqual(f.hash_table["c"], 200, msg="count for 'c' incorrect ")
        self.assertEqual(f.hash_table["d"], 1, msg="count for 'd' incorrect ")
        self.assertEqual(f.hash_table["e"], 10, msg="count for 'e' incorrect ")
        with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
            elt = f.hash_table["z"]

        self.assertEqual(f.max, 1500, msg=" max count is incorrect")
        self.assertEqual(f.most_common_word, 'a', msg=" incorrect max word")

    def test_rarity(self):
        # Checking if the rarity scores of individual words are correct.
        x = Freq()
        x.add_file("testfile_task6.txt")

        self.assertEqual(x.rarity("a"), 0, msg="count for 'a' incorrect")
        self.assertEqual(x.rarity("b"),0, msg="count for 'b' incorrect")
        self.assertEqual(x.rarity("c"), 0, msg="count for 'c' incorrect")
        self.assertEqual(x.rarity("d"), 2, msg="count for 'd' incorrect")
        self.assertEqual(x.rarity("e"), 1, msg="count for 'e' incorrect")
        self.assertEqual(x.rarity("z"), 3, msg="count for 'z' incorrect (supposed to be misspelled word) ")


if __name__ == '__main__':
  unittest.main()
