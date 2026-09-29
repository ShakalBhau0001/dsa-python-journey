# Problem No.136
# https://leetcode.com/problems/single-number

# Solution 1

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# Solution 2

import functools
import operator


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return functools.reduce(operator.xor, nums, 0)
