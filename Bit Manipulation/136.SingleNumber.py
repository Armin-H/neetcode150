from typing import List 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """first attempt solution same as neetcode's"""
        res = 0
        for n in nums:
            res ^= n
        return res
    
    def singleNumber(self, nums: List[int]) -> int:
        """my pythonic solution"""
        from operator import xor
        from functools import reduce
        return reduce(xor, nums)
