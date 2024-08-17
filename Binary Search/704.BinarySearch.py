from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """my first attempt solution. took me around 20 minutes to code"""
        l,r = 0,len(nums)-1

        while l <= r:

            middle_idx = (r+l) // 2
            middle = nums[middle_idx]
            if middle == target: 
                return middle_idx
            elif middle > target: 
                r = middle_idx - 1
            elif middle < target: 
                l = middle_idx + 1
        return -1
            

    def search(self, nums: List[int], target: int) -> int:
        """neetcode's solution except for the line with the comment"""
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow(doesn't happend in python)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
