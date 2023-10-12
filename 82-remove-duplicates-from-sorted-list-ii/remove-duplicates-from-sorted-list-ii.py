# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pp = None
        cp = head
        np = cp.next if cp != None else None

        while cp != None:
            cv = cp.val
            nv = np.val if np != None else None
            
            flag = True if cv == nv else False
            
            while nv == cv:
                cp.next = np.next
                np = cp.next
                nv = np.val if np != None else None
            
            if flag:
                if pp != None:
                    pp.next = np
                    cp = np
                    np = cp.next if cp != None else None
                else:
                    head = np
                    cp = np
                    np = cp.next if cp != None else None
            else:
                pp = cp
                cp = np
                np = cp.next if cp != None else None
        
        return head

