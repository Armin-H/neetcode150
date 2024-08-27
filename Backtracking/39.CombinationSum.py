from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """my first attempt solution, took me 45 minutes.
        There are other variatinos of this problem Combination Sum II,Combination Sum III,Combination Sum IV.
        I think my solution is more understandable than neetcode's solution.
        But his solution has interesting pattern and therefore is important to understand."""
        self.res = []

        def dfs(i,curr_comb,target):

            if i >= len(nums):
                return

            n = 0
            while True:
                r = target - n * nums[i]

                if r == 0:
                    self.res.append(curr_comb+n*[nums[i]])
                    return
                elif r < 0:
                    return 
                elif r > 0:
                    dfs(i+1,curr_comb + n*[nums[i]], r)
                    n += 1

        dfs(0,[],target)
        return self.res
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """neetcode's solution. The difference between my solution and neetcode's solution is that : 
        my decision tree in level i is deciding how many times to include nums[i] should be included.
        both neetcode's decision tree is more complex."""
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res