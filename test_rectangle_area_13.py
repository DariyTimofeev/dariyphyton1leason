import unittest
from rectangle_area_13 import rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(rectangle_area(5, 3), 15)

    def test_large_numbers(self):
        self.assertEqual(rectangle_area(1000, 2000), 2000000)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            rectangle_area(-5, 3)