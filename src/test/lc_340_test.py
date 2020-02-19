#!/usr/bin/env python
# coding=utf-8

import unittest
from leetcode.lc_340 import Solution


class LC340Case(unittest.TestCase):
    def test_res(self):
        s = Solution()
        res = s.lengthOfLongestSubstringKDistinct("eceba", 2)
        self.assertEqual(res[0], 3)
        self.assertEqual(res[1], "ece")


