from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """my recursive solution. coming up with the recursive solution was very easy, I should work on the iterative approach."""

        self.k_mins = []

        def inorder(node): 
            
            if not node: 
                return
            inorder(node.left)
            if len(self.k_mins) == k: 
                return
            self.k_mins.append(node.val)
            inorder(node.right)    

        inorder(root)

        return self.k_mins[-1]
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """neetcode's iterative solution"""
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right