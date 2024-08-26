# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """my solution. I'm using recersion while neetcode is using while loop.
        The time compleixy in the worse case is O(N) and the space complexity is O(1).
        but neetcode said that it's log(N) which is wrong when the tree is scwewed to one side"""

        if p.val == root.val or q.val == root.val: 
            return root
        
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right,p,q)
        else: 
            return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            """neetcode's solution"""
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root