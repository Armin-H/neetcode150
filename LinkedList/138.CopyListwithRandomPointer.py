"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """my solution(beated 94% on leetcode). Time complexity: O(N) (two passes over the linked list)
        ,Space Complexity O(N) because of the old2new dictionary."""
        if not head : 
            return None

        dummy = Node(0)

        curr = head
        newCurr = dummy
        old2new = dict()
        while curr: 
            newCurr.next = Node(curr.val, None, None)
            newCurr = newCurr.next
            old2new[curr] = newCurr
            curr = curr.next
        

        curr = head 
        newCurr = dummy.next
        while curr : 
            newCurr.random = old2new[curr.random] if curr.random else None
            curr = curr.next
            newCurr = newCurr.next

        return dummy.next