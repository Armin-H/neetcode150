# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """my first attempt solution. beated 99.4% of the solutions on leetcode"""
        nodes = []

        curr = head
        while curr: 
            nodes.append(curr)
            curr = curr.next

        if len(nodes) == n: 
            return head.next

        for _ in range(n):
            nth = nodes.pop()
        
        if not nodes: 
            return head.next
        node = nodes.pop()

        node.next = nth.next

        return head
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """neetcode's solution using two pointer approach"""
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next