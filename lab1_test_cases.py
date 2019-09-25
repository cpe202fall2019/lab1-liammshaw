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
        "tests to see if the general idea of the method works"
        tlist = [1,2,3,5,6,9,8,7,6,18,23,6,78,9]
        self.assertEqual(max_list_iter(tlist),78)

    def test_list_empty(self):
        "tests to see what happens if list is empty"
        tlist =[]
        self.assertEqual(max_list_iter(tlist),None)

    def test_max_first(self):
        "tests to see what happens when the largest number is first"
        tlist =[201,9,8,7,6,5,4,3,2,1]
        self.assertEqual(max_list_iter(tlist),201)

    def test_max_last(self):
        "test to see what happens when the largest number is last"
        tlist = [1,2,3,4,5,6,7,8,9,10,11,12,301]
        self.assertEqual(max_list_iter(tlist),301)

    #def test_reverse_rec(self):
        #self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    #def test_bin_search(self):
        #list_val =[0,1,2,3,4,7,8,9,10]
        #low = 0
        #high = len(list_val)-1
        #self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
