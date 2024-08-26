from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """my solution by using the helper function isSameTree(leetcode 100).
        I'm using a stack to traverse the tree but neetcode is using recursion."""
        def isSameTree(p,q): 
            if not p and not q: 
                return True
            elif not p or not q or p.val != q.val: 
                return False
            else: 
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

        if not subRoot: 
            return True

        stack = [root]
        while stack: 
            node = stack.pop()
            if isSameTree(node, subRoot):
                return True
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """neetcode's solution"""
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False