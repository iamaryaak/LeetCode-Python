# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return list with all odd indicies, then even indicies
        # solve in O(1) = cannot create array/new list
        # solve in O(n) = go in one take
        
        if not head:
            return None
        
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            # update odd list
            odd.next = even.next
            odd = odd.next
            # update even list
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        return head
            
        
        
            
