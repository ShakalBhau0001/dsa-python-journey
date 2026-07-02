# HashTable Approach 1

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return []

# HashTable Approach 2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            need = target - nums[i]
            if (need in d.keys and d[need]!=i):
                return [i,d[need]]

# Brute Force Approach 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i,j]

# Brute Force Approach 2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            need = target - nums[i]
            if (need in nums and nums.index(need)!=i):
                return [i,nums.index(need)]

# EOF
