import unittest
import sys
import os

# Ajout du répertoire source au path pour l'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()