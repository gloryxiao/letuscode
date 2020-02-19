#!/usr/bin/env python
# coding=utf-8

"""
题目描述
给定一个字符串，找到最长的包含最多k个不同字符的子串，输出最长子串的长度即可。

Example：

给出字符串”eceba”，k = 2

输出答案3，最长包含最多2个不同字符的子串为”ece”
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0

        sentry_start = sentry_end = 0
        max_sub_len = 0
        index_map = {}
        sub_start = 0
        for sub_end, value in enumerate(s):
            if len(set(s[sub_start:sub_end + 1])) > k:
                sub_start_value = s[sub_start]
                sub_start = index_map[sub_start_value] + 1

            index_map[value] = sub_end
            if max_sub_len < sub_end - sub_start + 1:
                max_sub_len = sub_end - sub_start + 1
                sentry_start = sub_start
                sentry_end = sub_end

        return max_sub_len, s[sentry_start:sentry_end+1]
