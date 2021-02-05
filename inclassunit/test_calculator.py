#to run the file please type: python test.py calculator.py
#should run each method and show if it failed or not
import unittest
from calculator import calculator

class Testcalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()
    def test_addition(self):
        self.assertEqual(self.calculator.addition(5,6), 11)
        
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5,6), -1)
        
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(5,6), 30)
        
    def test_division(self):
        self.assertEqual(self.calculator.division(30,6), 5)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

