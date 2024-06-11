from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #my solution
        numset = {}

        for i,n in enumerate(nums): 
            if n in numset:
                return [numset[n],i]
            else: 
                numset[target-n] = i

