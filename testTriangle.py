import unittest as utest
from triangle import Triangle

class TestTriangle(utest.TestCase):
    # Test 1
    def test_equilateral_triangle(self):
        result = Triangle.Logic(5, 5, 5)
        if result == "Equilateral tiangle":
            print("\033[32m\033[40m")
            print("Test 1 success")
            print("\033[37m\033[40m")
        else:
            print("\033[31m\033[40m")
            print("Test 1 failure")
            print("\033[37m\033[40m")
    # Test 2
    def test_isosceles_triangle(self):
        result = Triangle.Logic(7, 7, 10)
        if result == "Isosceles triange":
            print("\033[32m\033[40m")
            print("Test 2 success")
            print("\033[37m\033[40m")
        else:
            print("\033[31m\033[40m")
            print("Test 2 failure")
            print("\033[37m\033[40m")
    # Test 3
    def test_versatile_triangle(self):
        result = Triangle.Logic(3, 4, 5)
        if result == "Versatile triangle":
            print("\033[32m\033[40m")
            print("Test 3 success")
            print("\033[37m\033[40m")
        else:
            print("\033[31m\033[40m")
            print("Test 3 failure")
            print("\033[37m\033[40m")
    # Test 4
    def test_not_a_triangle(self):
        result = Triangle.Logic(0, 0, 0)
        if result == "Theres no triangle like this":
            print("\033[32m\033[40m")
            print("Test 4 success")
            print("\033[37m\033[40m")
        else:
            print("\033[31m\033[40m")
            print("Test 4 failure")
            print("\033[37m\033[40m")

if __name__ == '__main__':
    utest.main()