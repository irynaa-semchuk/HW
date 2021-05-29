import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(3, 9), 12)
        self.assertEqual(Calculator.add(2, 9), 11)
        self.assertEqual(Calculator.add(9, -1), 8)

    def test_add_negative_case(self):
        result = Calculator.add(-5, -6)
        self.assertNotEqual(result, 11)
        with self.assertRaises(TypeError):
            Calculator.add([1, 2], 5)
            Calculator.add('f', 5)
            Calculator.add(None, 5)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(9, 8), 1)
        self.assertEqual(Calculator.subtract(9, 7), 2)
        self.assertEqual(Calculator.subtract(9, 6), 3)

    def test_subtract_negative_case(self):
        result = Calculator.subtract(-5, -6)
        self.assertNotEqual(result, -1)
        with self.assertRaises(TypeError):
            Calculator.subtract([5, 2], 10)
            Calculator.subtract('9', 5)
            Calculator.subtract(None, 9)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(3, 3), 9)
        self.assertEqual(Calculator.multiply(2, 5), 10, "Should be 10")
        self.assertEqual(Calculator.multiply('h', 2), 'hh')

    def test_multiply_negative_case(self):
        result = Calculator.multiply(-5, 8)
        self.assertNotEqual(result, 40)
        with self.assertRaises(TypeError):
            Calculator.multiply([3, 6], (5, 8))
            Calculator.multiply((9, 10), 5)
            Calculator.multiply(None, (8, 9))

    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 2), 3)
        self.assertEqual(Calculator.divide(12, 2), 6)
        self.assertEqual(Calculator.divide(30, 2), 15)

    def test_divide_negative_case(self):
        result = Calculator.add(-5, -2)
        self.assertNotEqual(result, -2.5)
        with self.assertRaises(TypeError):
            Calculator.divide((1, 2), 9)
            Calculator.divide('f', 5)
            Calculator.divide(None, 5)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)
            Calculator.divide(4.8, 0)
            Calculator.divide(-8, 0)



if __name__ == '__main__':
    unittest.main()
