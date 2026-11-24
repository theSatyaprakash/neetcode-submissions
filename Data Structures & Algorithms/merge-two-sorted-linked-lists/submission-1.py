# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode()
        t=dum
        while l1 and l2:
            if l1.val <l2.val:
                t.next=l1
                l1=l1.next
            else:
                t.next=l2
                l2=l2.next
            t=t.next
        if l1:
            t.next=l1
        else:
            t.next=l2
        return dum.next


