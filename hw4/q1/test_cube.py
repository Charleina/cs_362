#
import unittest
from cube import cube

class Testcube(unittest.TestCase):
    def setUp(self):
        self.cube = cube()
        
    def test_cube1(self):
        self.assertEqual(self.cube.cube1(5,54,5), 1350)
        
    def test_cube2(self):
        self.assertEqual(self.cube.cube2(7,53,6.3), 2337)
        
    def test_cube3(self):
        self.assertEqual(self.cube.cube3(-9,(3/2),56), -756)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
