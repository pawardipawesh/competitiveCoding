# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        p1 = head
        p2 = head.next
        p3 = p2.next if p2 != None else None
        head.next= None
        
        while p2 != None:
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next if p3 != None else None
        
        return p1
        