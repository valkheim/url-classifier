#!/usr/bin/env python
import unittest
from features import subdomains


class TestSubdomains(unittest.TestCase):

    def test_subdomains(self):
        self.assertEqual(subdomains.get("test"), 0)
        self.assertEqual(subdomains.get("abd.def"), 0)
        self.assertEqual(subdomains.get("abd.def.ghi"), 0)
        self.assertEqual(subdomains.get("scheme://sub.domain.tld/"), 1)
        self.assertEqual(subdomains.get("scheme://sub.sub.domain.tld/"), 2)

    def test_parameters(self):
        self.assertEqual(subdomains.get(""), 0)
        self.assertEqual(subdomains.get(None), 0)


if __name__ == "__main__":
    unittest.main()
