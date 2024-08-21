from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """my recursive solution. Neetcode's solution is exactly the same. this is the recursive DFS solution."""
        if not root: 
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """neetcode's BFS solution. This was a good one to think about"""
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """neetcode's post-oder non-resursive DFS solution(In the video he says this is pre-oder but I think this is post-order because he is adding the left node to the stack first first).
        This is also a good one to think about.
        In this solution he is also adding Null nodes to the stack"""

        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res