from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Time complexity : O(n), Space complexity O(n)
        return True if len(set(nums)) != len(nums) else False

    def containsDuplicate(self, nums: List[int]) -> bool: 
        #neetcode's solution(i was able to come up with this exact solution)
        #Time complexity : O(n), Space complexity: O(n)
        #This solution has a better best-cast time and space complexity than the previous solution
        hashset = set()
        
        for n in nums: 
            if n in hashset: 
                return True
            else: 
                hashset.add(n)
        return False