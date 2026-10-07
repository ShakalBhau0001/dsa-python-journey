# Problem No.20
# https://www.leetcode.com/valid-parentheses

# Solution 1:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack

# Solution 2:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(","}": "{","]": "[",}
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0
