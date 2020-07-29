#!/usr/bin/env python3
"""
:author: Graeme Gange
"""
import math
import unittest
import task1

class TestHashTable(unittest.TestCase):
  def test_init(self):
    x = task1.HashTable()
    y = task1.HashTable(10)
    z = task1.HashTable(800, 2398)

  def test_hash(self):
    x = task1.HashTable(1024, 1)

    for (key, expect) in [("", 0),
                          ("abcdef", 597),
                          ("defabc", 597)]:
        self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 1 and key {key}.")

    x = task1.HashTable(1024, 17)
    for (key, expect) in [("", 0),
                          ("abcdef", 389),
                          ("defabc", 309)]:
        self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 17 and key {key}.")

  # The tests for __contains__ and __getitem__ use __setitem__, so we don't make any assumptions
  # about the underlying array representation. Remember to define your own tests for __setitem__
  # (and rehash)
  def test_contains(self):
    x = task1.HashTable(1024, 1)

    self.assertFalse("abcdef" in x, "False positive in __contains__ for empty table.")

    x["abcdef"] = 18
    x["definitely a string"] = None
    x["abdcef"] = "abcdef"
    
    for key in ["abcdef", "definitely a string", "abdcef"]:
      self.assertTrue(key in x, f"False negative in __contains__ for key {key}")

    self.assertFalse("defabc" in x, "False positive due to collision.")

  def test_getitem(self):
    x = task1.HashTable(1024, 1)

    with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
      elt = x["abcdef"]
      
    x["abcdef"] = 18
    x["definitely a string"] = None

    self.assertEqual(x["abcdef"], 18, msg = "Read after write failed.")
    self.assertEqual(x["definitely a string"], None, "Failed to retrieve written None.")

    x["abdcef"] = 22

    self.assertEqual(x["abcdef"], 18, msg = "Key overwritten by colliding value.")
    self.assertEqual(x["abdcef"], 22, msg = "Failed to write colliding value.")

    with self.assertRaises(KeyError, msg="False positive from colliding key."):
      elt = x["defabc"]

if __name__ == '__main__':
  unittest.main()
