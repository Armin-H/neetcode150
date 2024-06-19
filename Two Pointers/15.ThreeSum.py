from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """my solution. Idea : sort then set target to the -firstItem of the list and reduce the problem to TwoSum2.
        time complexity : O(n^2) """
        sortedNums = sorted(nums)
        res = []

        for i in range(len(nums) - 2): 
           
            if i > 0 and sortedNums[i] == sortedNums[i-1]: 
                print(i)
                continue
            
            l,r = i+1,len(nums)-1

            while l < r: 
                currSum = sortedNums[l] + sortedNums[r]
                target = sortedNums[i]
                if currSum > -target: 
                    r-= 1
                elif currSum < -target: 
                    l+= 1
                else: 
                    res.append([target,sortedNums[l],sortedNums[r]])
                    l += 1
                    while sortedNums[l] == sortedNums[l-1] and l < r:
                        l += 1
                    r -= 1

        return res
        

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """neetcode's solution, same as mine"""
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
