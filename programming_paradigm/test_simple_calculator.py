import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calculator = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(3, 5), -2)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(5, 0), None)  # Division by zero should return None
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
    def test_divide_negative(self):
        """Test the division method with negative numbers."""
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        self.assertEqual(self.calculator.divide(6, -3), -2)
        self.assertEqual(self.calculator.divide(-6, -3), 2)
    def test_divide_float(self):
        """Test the division method with float numbers."""
        self.assertAlmostEqual(self.calculator.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calculator.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calculator.divide(5.0, 0), None)
    def test_divide_invalid(self):
        """Test the division method with invalid inputs."""
        with self.assertRaises(TypeError):
            self.calculator.divide("a", 2)
        with self.assertRaises(TypeError):
            self.calculator.divide(2, "b")
        with self.assertRaises(TypeError):
            self.calculator.divide("a", "b")
if __name__ == '__main__':
    unittest.main()
# This code is a unit test for the SimpleCalculator class.
# It tests the basic arithmetic operations: addition, subtraction, multiplication, and division.
# The tests cover normal cases, edge cases like division by zero, and invalid inputs.
# The unittest framework is used to run the tests and check for expected outcomes.
# The test cases ensure that the SimpleCalculator class behaves as expected for various inputs.
# The tests include checks for both positive and negative numbers, as well as float values.
# The code is designed to be run as a script, and it will execute the tests when run directly.
# The test cases ensure that the SimpleCalculator class behaves as expected for various inputs.
# The tests include checks for both positive and negative numbers, as well as float values.
# The code is designed to be run as a script, and it will execute the tests when run directly. 