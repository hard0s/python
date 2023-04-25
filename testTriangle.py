import unittest as utest
from triangle import Triangle

class TestTriangle(utest.TestCase):
    # Test 1
    def test_equilateral_triangle(self):
        result = Triangle.Logic(5, 5, 5)
        self.assertEqual(result, None)
    # Test 2
    def test_isosceles_triangle(self):
        result = Triangle.Logic(7, 7, 10)
        self.assertEqual(result, None)
    # Test 3
    def test_versatile_triangle(self):
        result = Triangle.Logic(3, 4, 5)
        self.assertEqual(result, None)
    # Test 4
    def test_not_a_triangle(self):
        result = Triangle.Logic(0, 0, 0)
        self.assertEqual(result, None)
if __name__ == '__main__':
    utest.main()