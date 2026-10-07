# Problem No.125
# https://leetcode.com/problems/valid-palindrome


# Solution 1:

class Solution:
    def isPalindrome(self, string):
        clean = ""
        for char in string:
            if char.isalnum():
                clean += char.lower()

        reverse = ""
        for char in clean:
            reverse = char + reverse

        return reverse == clean

# Solution 2:

class Solution:
    def isPalindrome(self, string):
        clean = ""
        for char in string:
            if char.isalnum():
                clean += char.lower()

        reverse = ""
        for char in clean:
            reverse = char + reverse

        if reverse == clean:
            return True
        else:
            return False
