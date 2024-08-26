from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """my solution, the idea is the same as 543
        I think the name of the inner function height is not very appropriate and can be improved.
        I think my solution is more readable than the neetcode's solution."""
        self.is_balanced = True

        def height(node): 
            if not node: 
                return 0  

            lh = height(node.left)
            rh = height(node.right)
            if abs(lh-rh) > 1: 
                self.is_balanced = False
            return max(rh,lh) + 1
        
        height(root)
        return self.is_balanced
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """neetcode's solution"""
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]