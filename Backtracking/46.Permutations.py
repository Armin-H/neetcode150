from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """my solution. Time complexity is O(n! * n^2) which is basically O(n!)"""
        if len(nums) == 1: 
            return [nums]

        res = []

        for p in self.permute(nums[1:]):
            for i in range(len(p)+1):
                res.append(p[:i] + [nums[0]] + p[i:])

        return res
    

    def permute(self, nums: List[int]) -> List[List[int]]:
        """neetcode's recursive solution(this is different than what he showed in the video)."""
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        """neetcode's iterative solution"""
        perms = [[]]

        for n in nums: 
            new_perms = []
            for p in perms: 
                for i in range((len(p)+1)): 
                    p_copy =p.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perms = new_perms

        return perms