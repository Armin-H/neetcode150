from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """my first attempt DP solution. Time and Space complexity is O(n)"""
        if len(nums) <= 2:
            return max(nums)

        DP = [0] * len(nums)
        DP[0] = nums[0]
        DP[1] = nums[1]
        DP[2] = max(nums[1], nums[0] + nums[2])
        for i in range(3,len(nums)): 
            DP[i] = max(DP[i-1], nums[i]+DP[i-2], nums[i]+DP[i-3])

        return DP[-1]
    
    def rob(self, nums: List[int]) -> int:
        """my another DP solution but this time using nums array itself, which makes the space complexity O(1)"""
        
        if len(nums) <= 2:
            return max(nums)

        nums[2] = max(nums[1],nums[0] + nums[2])

        for i in range(3,len(nums)): 
            nums[i] = max(nums[i-1], nums[i]+nums[i-2], nums[i]+nums[i-3])

        return nums[-1]
    
    def rob(self, nums: List[int]) -> int:
        """neetcode's solution. This solution is more simple than mine"""
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
