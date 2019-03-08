#!/usr/bin/env python
import unittest
from features import tld


class TestTld(unittest.TestCase):

    def test_tld(self):
        self.assertEqual(tld.get("schema://domain.tld"), "tld")
        self.assertEqual(tld.get("schema://domain.non_existent_tld"), "non_existent_tld")
        self.assertEqual(tld.get("http://example.com"), "com")

    def test_parameters(self):
        self.assertEqual(tld.get("test"), None)
        self.assertEqual(tld.get(""), None)


if __name__ == "__main__":
    unittest.main()
