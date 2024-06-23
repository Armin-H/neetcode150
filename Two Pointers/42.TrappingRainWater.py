from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        """My solution, time complexity: O(n), space complexity : O(n)"""
        if len(height) <= 2 : 
            return 0
        
        left = None
        is_peak = [False] * len(height)
        for i in range(len(height)): 
            if left is None:
                if height[i] > 0: 
                    is_peak[i] = True
                    left = i 
            else: 
                if height[i] >= height[left]:
                    is_peak[i] = True
                    left = i
        
        right = None
        for i in reversed(range(len(height))): 
            if right is None:
                if height[i] > 0: 
                    is_peak[i] = True
                    right = i
            else: 
                if height[i] >= height[right]: 
                    is_peak[i] = True
                    right = i
            

        left = None
        intervals = []
        for i in range(len(is_peak)): 
            if left is None:
                if is_peak[i]:
                    left = i
            else: 
                if is_peak[i]: 
                    right = i 
                    intervals.append([left,right])
                    left = right
        total = 0
        
        for l,r in intervals: 
            if r-l < 2: 
                continue
            else: 
                h = min(height[l],height[r])
                total += (r-l-1) * h -sum(height[l+1:r])
        
        return total

    def trap(self, height: List[int]) -> int:
        """neetcode's solution. Time complexity : O(n), space Complexity : O(1)"""
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
