from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """my solution. I believe although my solution is shorter and more understandable, it's important to understand neetcode's solution."""
        
        if len(nums) == 1: 
            return [nums,[]]

        res = []
        for i in [[nums[0]],[]]: 
            for j in self.subsets(nums[1:]): 
                res.append(i+j)

        return res
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """neetcode's solution.
        This solution is confusing to me and I don't quite understand the DFS part.
        I think the DFS is on the decision tree. And each leaf in the decision tree is an member of the subset."""
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            #decision to not include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res