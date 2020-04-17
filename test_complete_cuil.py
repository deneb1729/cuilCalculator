#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from modules.complete_cuil import completeCuil

mock_cuils = [["2036489026", 5, "20364890266"],
              ["2035824572", 8, "20358245723"],
              ["2028784875", 3, "20287848758"],
              ["2722621984", 10, "27226219841"],
              ["2735196499", 0, "27351964990"],
              ["2021578048", 9, "20215780482"],
              ["2018667907", 5, "20186679076"],
              ["2721823119", 0, "27218231190"],
              ["2714564917", 6, "27145649175"],
              ["2710009638", 3, "27100096388"],
              ["2737919086", 2, "27379190869"]]

class TestCompleteCuil(unittest.TestCase):
    def test_complete_cuil(self):
        for element in mock_cuils:
            self.assertEqual( completeCuil(element[0], element[1]), element[2])

if __name__ == "__main__":
    unittest.main()