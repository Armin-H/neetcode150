from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """my inefficient solution(TLE error on leetcode.com). time complexity: O(kn)"""
        result = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            result.append(max(window))

        return result
    
