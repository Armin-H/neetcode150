from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        "my iterative solution."
        if head is None or head.next is None: 
            return head
        
        prev = None
        curr = head
        next = curr.next

        while next: 
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        "neetcode's iterative solution. "
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """neetcode's recursive solution.
        I don't understand this"""
        if not head: 
            return None

        newHead = head
        if head.next: 
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead