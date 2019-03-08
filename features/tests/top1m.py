#!/usr/bin/env python
import unittest
from features import top1m


class TestTop1M(unittest.TestCase):

    def test_websites(self):
        self.assertEqual(top1m.get("http://google.com"), 1)

    def test_parameters(self):
        self.assertEqual(top1m.get(""), 0)


if __name__ == "__main__":
    unittest.main()
