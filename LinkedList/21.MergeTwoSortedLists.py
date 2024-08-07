from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """my solution.
        Neetcode's solution in his video is exactly the same as mine."""
        head = ListNode()
        curr = head
        while list1 and list2: 
            if list1.val <= list2.val: 
                curr.next = list1
                list1 = list1.next
            else: 
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        if list1: 
            curr.next = list1
        elif list2: 
            curr.next = list2

        return head.next

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """neetcode's solution"""
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next