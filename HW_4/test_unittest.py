import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(3, 9), 12)
        self.assertEqual(Calculator.add(2, 9), 11)
        self.assertEqual(Calculator.add(1, 9), 10)
        self.assertRaises(TypeError, Calculator.add, [1, 2], 5)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(9, 8), 1)
        self.assertEqual(Calculator.subtract(9, 7), 2)
        self.assertEqual(Calculator.subtract(9, 6), 3)
        self.assertRaises(TypeError, Calculator.add, [5, 2], 10)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(3, 3), 9)
        self.assertEqual(Calculator.multiply(2, 5), 10, "Should be 10")
        self.assertRaises(TypeError, Calculator.multiply, [3, 6], 5)

    def test_divide(self):
        self.assertEqual(Calculator.divide(2, 6), 3)
        self.assertEqual(Calculator.divide(2, 12), 6)
        self.assertEqual(Calculator.divide(2, 30), 15)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
