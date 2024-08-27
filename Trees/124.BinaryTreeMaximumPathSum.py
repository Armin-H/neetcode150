from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """my solution. The idea is very similar to 543 and 110.
        but it's more difficult to think why the algorithm gives correct answer."""
        self.max_sum = float('-inf')

        def dfs(node): 
            """updates max_sum but returns the max path from this node to the bottom of the tree"""

            if not node: 
                return 0 
            
            l_max_sum = dfs(node.left)
            r_max_sum = dfs(node.right)
            self.max_sum = max((self.max_sum , node.val + l_max_sum + r_max_sum,
                                node.val + l_max_sum,
                                node.val + r_max_sum,
                                node.val))

            return max((node.val + max(l_max_sum, r_max_sum),
                        node.val))
        
        dfs(root)
        return self.max_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """neetcode's solution. I like that he is setting the leftMax and rightMax to 0 if they are negative,
        It makes the max computations easier"""
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """somebody's solution in neetcode's comment. this is the same solution as ours but without using a global/non-local variable."""
        def dfs(root):
            if not root:
                return 0, float("-inf") 
            left, wl = dfs(root.left)
            left = max(left,0)
            
            right, wr = dfs(root.right)
            right = max(right,0)
            
            res = max(wl, wr, root.val+left+right)
            return root.val+max(left,right) , res

        return dfs(root)[1]