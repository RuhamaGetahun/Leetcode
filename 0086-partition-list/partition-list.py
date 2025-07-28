# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode()
        less = less_dummy 
        greater_dummy = ListNode()
        greater = greater_dummy 

        current = head 
        while current:
            if current.val < x:
                less.next = current 
                less = current 
                current = current.next 
            else:
                greater.next = current 
                greater = current
                current = current.next

        greater.next = None  # terminate the greater linked list last node   
        less.next = greater_dummy.next 
        return less_dummy.next 

            
        