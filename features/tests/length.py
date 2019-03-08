#!/usr/bin/env python
import unittest
from features import length


class TestLength(unittest.TestCase):

    def test_length(self):
        self.assertEqual(length.get("test"), 4)
        self.assertEqual(length.get(""), 0)

    def test_parameters(self):
        self.assertEqual(length.get(""), 0)
        self.assertEqual(length.get(None), 0)


if __name__ == "__main__":
    unittest.main()
