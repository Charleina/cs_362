import unittest
from leapyear import leapyear

class TestCase(unittest.TestCase):
    def setUp(self):
        self.leapyear = leapyear()
        
    def test1(self):
        self.assertEqual(self.leapyear.leapyear(), "True")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
