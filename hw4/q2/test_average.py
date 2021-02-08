#run the tests by typing python test_average.py last list is an empty one for testing purposes

import unittest
from average import average

l1 = [1,2,3,4,5,6,7,8]
l2 = [534,657,13,78,42]
l3 = []

class Testaverage(unittest.TestCase):
    def setUp(self):
        self.average = average()
        
    def test_average1(self):
        self.assertEqual(self.average.average1(l1), 4.5)
        
    def test_average2(self):
        self.assertEqual(self.average.average2(l2), 264.8)
        
    def test_average3(self):
        self.assertEqual(self.average.average3(l3), 0)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

