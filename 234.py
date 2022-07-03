# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # do this in linear time
        # create set to track values
        # remove if same value
        # if the set is empty, return true, else false
        valSet = []
        curr = head
        isPal = True
        while curr:
            valSet.append(curr.val)
            curr = curr.next
        if len(valSet) == 1:
            return True
            
        for i in range(len(valSet)//2):
            if valSet[i] != valSet[len(valSet)-i-1]:
                isPal = False
                break
        
        return isPal
