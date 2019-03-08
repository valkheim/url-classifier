#!/usr/bin/env python
import unittest
from features import daysSinceRegistration


class TestDaysSinceRegistration(unittest.TestCase):

    def test_daysSinceRegistration(self):
        self.assertTrue(daysSinceRegistration.get("example.com") >= 8607)
        self.assertTrue(daysSinceRegistration.get("http://example.com") >= 8607)

    def test_parameters(self):
        self.assertEqual(daysSinceRegistration.get(None), None)
        self.assertEqual(daysSinceRegistration.get(""), None)
        self.assertEqual(daysSinceRegistration.get("a_non_existent_domain_name_o_rly_r_u_sure_well_no.com"), None)

if __name__ == "__main__":
    unittest.main()
