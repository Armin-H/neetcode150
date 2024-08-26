from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """wasn't able to come up with the solution in 15 minutes, but I had the right ideas.
        I was obvious that we need a nested function, but I was confused about its return value, and what needs to be done with it.
        This solution is from neetcode."""
        self.diameter = 0 
        
        # returns height of the node and updates the diameter
        def dfs(node): 
            if not node: 
                return 0
                
            lheight = dfs(node.left)
            rheight = dfs(node.right)
            self.diameter = max(self.diameter, lheight + rheight)
            return max(lheight,rheight) + 1
        dfs(root)
        return self.diameter  