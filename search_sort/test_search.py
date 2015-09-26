import unittest
from search import Searches

class LinearSearchTest(unittest.TestCase):

    def setUp(self):
        self.friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
        self.search = Searches()

    def tearDown(self):
        del self.friends
        del self.search

    def test_linear_search_easy(self):
        self.assertEqual(self.search.linear(self.friends, "Zoe"), 1)

    def test_linear_search_start_index(self):
        self.assertEqual(self.search.linear(self.friends, "Joe"), 0)

    def test_linear_search_middle(self):
        self.assertEqual(self.search.linear(self.friends, "Paris"), 6)

    def test_linear_search_not_found(self):
        self.assertEqual(self.search.linear(self.friends, "Bill"), -1)

# Binary Search
class BinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
        self.search = Searches()

    def tearDown(self):
        del self.xs
        del self.search

    def test_binary_search_not_found(self):
        self.assertEqual(self.search.binary(self.xs, 20), -1)

    def test_binary_search_latter_end(self):
        self.assertEqual(self.search.binary(self.xs, 37), 10)

    def test_binary_search_beginning(self):
        self.assertEqual(self.search.binary(self.xs, 2), 0)

    def test_binary_search_middle(self):
        self.assertEqual(self.search.binary(self.xs, 23), 7)
