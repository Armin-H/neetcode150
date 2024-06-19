from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """bruteforce solution. time complexity : O(n^2)"""
        best = 0
        for i in range(len(heights)): 
            for j in range(i+1,len(heights)):
                best = max(best, (j-i) * min(heights[i],heights[j]))

        return best


    def maxArea(self, heights: List[int]) -> int:
        """my solution. Time complextiy : O(n^2)"""
        l,r = 0 , len(heights)-1
        currMax = min(heights[l],heights[r]) * (r-l)
        while l < r: 
            if heights[l] > heights[r]: 
                r -= 1
            elif heights[l] < heights[r]: 
                l += 1
            else: 
                l += 1
                r -= 1
            currMax = max(currMax, min(heights[l],heights[r]) * (r-l))
        return currMax


    def maxArea(self, heights: List[int]) -> int:
        """neetcode's solution"""
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
            
        return res
