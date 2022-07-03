# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Time: O(n)
        # Space: O(1)
        
        # first idea is to reverse a linked list (but that would take longer)
        # create dummy variable
        dummy = ListNode(0, head)
        # choose 2 pointers
        left = dummy
        right = head
        
        # set right pointer to be n ahead of left pointer
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # iterate until right is at the end of the list and return 
        while right:
            left = left.next
            right = right.next
        # left pointer is at the node thats supposed to be deleted
        left.next = left.next.next
        return dummy.next
