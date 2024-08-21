# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """my first attempt non-recursive solution."""
        queue = collections.deque()

        if root: 
            queue.append(root)
        else: 
            return None
        while queue: 
            node = queue.popleft()
            if node.left : queue.append(node.left)
            if node.right : queue.append(node.right)
            node.left, node.right = node.right, node.left

        return root
    

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """my first attempt recursive solution. Same as neetcode's solution, except that he doesn't check if the either of the children are None."""
        if root is None: 
            return None
        else: 
            root.left, root.right = root.right, root.left
            if root.left: self.invertTree(root.left) # we don't have to check if the left or right child is None
            if root.right: self.invertTree(root.right)

        return root
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """neetcode's solution"""
        if not root: return None

        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root