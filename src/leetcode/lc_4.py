#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def search_index(start, end):
            if start >= end:
                return start

            short_i = (start + end) / 2
            long_j = (len_1 + len_2 + 1) / 2 - short_i

            if search_one[short_i] >= long_one[long_j - 1]:
                if long_j == long_len:
                    return short_i

                if search_one[short_i - 1] <= long_one[long_j]:
                    return short_i
                else:
                    return search_index(start, short_i - 1)
            else:
                return search_index(short_i + 1, end)

        len_1, len_2 = len(nums1), len(nums2)
        search_one = nums1 if len_1 <= len_2 else nums2
        long_one = nums2 if len_1 <= len_2 else nums1
        search_len = len(search_one)
        long_len = len(long_one)
        result_i = search_index(0, search_len)
        result_j = (len_1 + len_2 + 1) / 2 - result_i
        if (len_1 + len_2) % 2 == 1:
            if result_i == 0:
                return long_one[result_j - 1]
            else:
                return max(search_one[result_i - 1], long_one[result_j - 1])
        else:
            if result_i == 0:
                if search_len == 0:
                    return (long_one[result_j - 1] + long_one[result_j]) / 2.0
                if result_j == long_len:
                    return (long_one[result_j - 1] + search_one[result_i]) / 2.0

                return (long_one[result_j - 1] + min(search_one[result_i], long_one[result_j])) / 2.0
            elif result_i == search_len:
                if result_j == 0:
                    return (search_one[result_i - 1] + long_one[result_j]) / 2.0
                else:
                    return (max(search_one[result_i - 1], long_one[result_j - 1]) + long_one[result_j]) / 2.0
            else:
                return (max(search_one[result_i - 1], long_one[result_j - 1]) + min(search_one[result_i], long_one[result_j])) / 2.0


if __name__ == "__main__":
    s = Solution()
    # a = s.findMedianSortedArrays([1, 3], [2])
    # a = s.findMedianSortedArrays([1], [-2, -1])
    # a = s.findMedianSortedArrays([1], [1])
    # a = s.findMedianSortedArrays([1,2], [1,1])
    a = s.findMedianSortedArrays([4], [1,2,3])
    print a
