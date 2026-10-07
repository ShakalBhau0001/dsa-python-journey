# Problem No. 13
# https://leetcode.com/problems/roman-to-integer

# Solution 1:

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res = res - roman[s[i]]
            else:
                res = res + roman[s[i]]
        return res


# Solution 2:

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        prev = 0

        for ch in reversed(s):
            value = roman[ch]

            if value < prev:
                total -= value
            else:
                total += value

            prev = value

        return total
