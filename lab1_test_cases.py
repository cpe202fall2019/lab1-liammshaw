import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests if list is none"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list(self):
        """tests to see if the general idea of the method works"""
        #tlist = [1,2,3,5,6,9,8,7,6,18,23,6,78,9]
        self.assertEqual(max_list_iter([1,2,3,5,6,9,8,7,6,18,23,6,78,9]),78)
        self.assertEqual(max_list_iter([1,2,3,4,5,6,7,8,9,12,23,4,18,0]),23)

    def test_list_empty(self):
        """tests to see what happens if list is empty"""
        tlist =[]
        self.assertEqual(max_list_iter(tlist),None)

    def test_max_first(self):
        """tests to see what happens when the largest number is first"""
        tlist =[201,9,8,7,6,5,4,3,2,1]
        self.assertEqual(max_list_iter(tlist),201)

    def test_max_last(self):
        """test to see what happens when the largest number is last"""
        tlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 301]
        self.assertEqual(max_list_iter(tlist), 301)

# testing reverse function

    def test_reverse_rec_01(self):
        """test the basics 01"""
        self.assertEqual(reverse_rec([3, 4, 5]), [5, 4, 3])
        self.assertEqual(reverse_rec([4, 4, 4]), [4, 4, 4])

    def testing_reverse_rec_one_number(self):
        """test one number lists"""
        self.assertEqual(reverse_rec([1]), [1])

    def test_empty_reverse_rec(self):
        """Tests empty list"""
        tlist = []
        self.assertEqual(reverse_rec(tlist),[])

    def test_reverse_value_error_rec(self):
        """tests if list is none"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

# Testing binary search
    def test_bin_search(self):
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search(self):
        list_val =[0, 1, 2, 3]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3)

    def test_bin_search(self):
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

    def test_bin_search_no_numbers(self):
        list_val = []
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(None, 0, len(list_val) - 1, list_val), None)

    def test_bin_search_missing_target(self):
        list_val = [1, 2, 3, 4, 5, 6]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), None)


if __name__ == "__main__":
        unittest.main()

    
