#!/usr/bin/env python
import unittest
from features import top1m
from data import data

class TestTop1M(unittest.TestCase):

    dt = data.Data()

    def test_websites(self):
        self.assertEqual(top1m.get("http://google.com", self.dt.data), 1)

    def test_parameters(self):
        self.assertEqual(top1m.get("", self.dt.data), 0)

    def test_badValues(self):
        self.assertEqual(top1m.get("google.com", self.dt.data), 0)
        self.assertEqual(top1m.get("http://google.non_existent_tld", self.dt.data), 0)


if __name__ == "__main__":
    unittest.main()
