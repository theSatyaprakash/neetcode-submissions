# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self,l1,l2):
            dum=ListNode()
            tail=dum
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next=l1
                    tail=tail.next
                    l1 = l1.next
                else:
                    tail.next=l2
                    tail=tail.next
                    l2 = l2.next
            if l1:
                tail.next=l1
                tail=tail.next
                l1 = l1.next
            if l2:
                tail.next=l2
                tail=tail.next
                l2 = l2.next
            return dum.next
    def mergeKLists(self, l: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(l)==0:
            return None
        while len(l)>1:
            mergelist=[]
            for i in range(0,len(l),2):
                l1=l[i]
                l2=l[i+1] if (i+1)<len(l) else None
                mergelist.append(self.merge(l1,l2))
            l=mergelist
        return l[0]

        


    
            

















        