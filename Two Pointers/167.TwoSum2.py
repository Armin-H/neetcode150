from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """my solution. Time complexity : O(n)"""
        l,r = 0, len(numbers)-1
        #we can have True as the condition because the problem garantees a solution
        while True: 
            a = numbers[l]
            b = numbers[r]
            if a + b > target: 
                r -= 1
            elif a + b < target: 
                l += 1
            else: 
                return [l+1,r+1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """neetcode's solution(same as mine but cleaner)"""
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
