from typing import List, Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """my solution. similar to 104 bfs solution.
        Neetcode's solution is very similar but I like my solution more"""
        
        if not root: 
            return []

        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            res.append([]) 
            for i in range(len(queue)): 
                node = queue.popleft()
                res[-1].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """neetcode's solution"""
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res