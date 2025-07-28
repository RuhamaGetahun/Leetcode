# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        dummy = ListNode()
        dummy.next = head

        if not head or not head.next: 
            return head 

        prev, current = dummy, head 
        while current and current.next:
            next_ = current.next 
            # swapping happens 
            prev.next = next_ 
            current.next = next_.next 
            next_.next = current 
            
            # skip to the next adjacents 
            prev = current 
            current = current.next 

        return dummy.next 
