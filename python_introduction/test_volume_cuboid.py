from volume_cuboid import *
import unittest

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),0)
        self.assertAlmostEqual(cuboid_volume(2),8)
    def test_input_value(self):
        self.assertRaises(TypeError, cuboid_volume, True)
class TestCuboidVolume(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(cuboid_volume(3), 27)
        self.assertEqual(cuboid_volume(0), 0)
        self.assertEqual(cuboid_volume(-2), -8)

    def test_valid_float(self):
        self.assertAlmostEqual(cuboid_volume(1.5), 3.375)
        self.assertAlmostEqual(cuboid_volume(-1.2), -1.728  )

    def test_invalid_type_str(self):
        with self.assertRaises(TypeError):
            cuboid_volume('two')

    def test_invalid_type_complex(self):
        with self.assertRaises(TypeError):
            cuboid_volume(2j)

    def test_invalid_type_bool(self):
        with self.assertRaises(TypeError):
            cuboid_volume(True)

    def test_invalid_type_list(self):
        with self.assertRaises(TypeError):
            cuboid_volume([2])


if __name__ == '__main__':
    unittest.main()
# This code is a unit test for the cuboid_volume function.
# It checks various cases including valid integers, floats, and invalid types.
# The test cases ensure that the function behaves correctly and raises appropriate exceptions for invalid inputs.
# The test cases are organized into a class that inherits from unittest.TestCase.
# The unittest framework is used to run the tests and report results.
# The test cases cover a range of scenarios to ensure robustness and correctness of the cuboid_volume function.
# The test cases are designed to be comprehensive, covering both valid and invalid inputs.
# The unittest framework provides a structured way to define and run tests, making it easier to maintain and extend the test suite.     