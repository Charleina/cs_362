#type python test_full_name.py to compile and run the tests

import unittest
from full_name import full_name

first1 = "Charlene"
last1 = "Wang"
first2= "John"
last2= "Smith"
first3= ""
last3= ""


class Testfull_name(unittest.TestCase):
    def setUp(self):
        self.full_name = full_name()
        
    def test_full_name1(self):
        self.assertEqual(self.full_name.full_name1(first1, last1), "Charlene Wang")
        
    def test_full_name2(self):
        self.assertEqual(self.full_name.full_name1(first2, last2), "John Smith")
        
    def test_full_name3(self):
        self.assertEqual(self.full_name.full_name1(first3, last3), "")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
