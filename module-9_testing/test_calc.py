import unittest
from calc import *


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(10, 5), 15)
        self.assertEquals(add(1, -1), 0)
        self.assertEquals(add(-1, -1), -2)

    def test_sub(self):
        self.assertEquals(sub(10, 5), 5)
        self.assertEquals(sub(-1, 1), -2)
        self.assertEquals(sub(-1, -1), 0)

    def test_mul(self):
        self.assertEquals(mul(10, 5), 50)
        self.assertEquals(mul(1, -1), -1)
        self.assertEquals(mul(-1, -1), 1)

    def test_div(self):
        self.assertEquals(div(10, 5), 2)
        self.assertEquals(div(1, -1), -1)
        self.assertEquals(div(-1, -1), 1)

        self.assertRaises(ValueError, div, 10, 0)


if __name__ == "__main__":
    unittest.main()
