from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """my solution. Neetcode's solution is more compact and more readable."""
        
        if p is None and q is None: 
            return True
        elif p is None and q is not None: 
            return False
        elif p is not None and q is None: 
            return False
        else: 
            if p.val == q.val:
                if (self.isSameTree(p.left,q.left) and 
                    self.isSameTree(p.right, q.right)): 
                    return True
                else: 
                    return False
            else: 
                return False
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """neetcode's solution"""
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False