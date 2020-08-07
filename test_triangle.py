import unittest
from triangle import checkTriangle


class MyTestCase(unittest.TestCase):
    def testValidity(self):
        self.assertEqual(checkTriangle(1, 1, 2), "Triangle not valid")

    def testIntegerValues(self):
        self.assertEqual(checkTriangle(-1, 4, 2), "Negative integer(s) found")

    def testScalene(self):
        self.assertEqual(checkTriangle(2, 5, 4), "Scalene")

    def testIsosceles(self):
        self.assertEqual(checkTriangle(4, 4, 2), "Isosceles")

    def testEquilateral(self):
        self.assertEqual(checkTriangle(3, 3, 3), "Equilateral")


if __name__ == '__main__':
    unittest.main()
