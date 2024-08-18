from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """my first attempt solution. I think the conditions of the if statements can be improved"""
        l,r = 0, len(nums)-1

        while l <= r: 
            m = (l+r) // 2
            if nums[l] <= nums[m] <= nums[r]: 
                return nums[l]
            elif nums[l] >= nums[m] <= nums[r]: 
                r = m
            elif nums[l] <= nums[m] >= nums[r]: 
                l = m + 1

    def findMin(self, nums: List[int]) -> int:
        """neetcode's solution. this is a little bit different that his code in his youtube."""
        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = start + (end - start ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])
    