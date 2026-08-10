# Problem No. 9

# Solution 1

class Solution(object):
    def isPalindrome(self,number):
        OriginalNumber = number
        s = 0
        while(number > 0):
            remainder = number % 10
            s = s * 10 + remainder
            number = number // 10

        if(s == OriginalNumber):
            return True
        else:
            return False

# Solution 2

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x
