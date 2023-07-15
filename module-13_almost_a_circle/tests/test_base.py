import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    # Test Base class using no arguments
    def test_no_args(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)


if __name__ == "__main__":
    unittest.main()