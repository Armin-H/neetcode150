from typing import List
from operator import xor
from functools import reduce
from itertools import chain
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """my first attempt solution"""
        if len(nums) == 1:
            return int(not nums[0])
        a = len(nums).bit_length()
        
        res = 0
        for n in nums:
            res ^= n

        for n in range(len(nums) + 1, 2 ** a):
            res ^= n 

        return res

    def missingNumber(self, nums: List[int]) -> int:
        """my pythonic solution, got the idea from neetcode's solution"""
        return reduce(xor, chain(range(len(nums)+1),nums))
    
    def missingNumber(self, nums: List[int]) -> int:
        """neetcode's math solution"""
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])

        return res