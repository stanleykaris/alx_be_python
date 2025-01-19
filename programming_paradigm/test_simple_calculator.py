# test_simple_calculator

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a simpleCalculator instance before each test."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 3), 3)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -3), 1)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.mulitply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 1), 0)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main() 