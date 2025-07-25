# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # let's solve this by using length first 
        length = 0
        current = head 
        while current:
            length += 1 
            current= current.next 

        target = length - n 
        if target == 0 : # if asked to delete the head of the linked list 
            return head.next 
        
        current = head 
        for i in range(target - 1):
            current = current.next 
        current.next = current.next.next 
        return head 