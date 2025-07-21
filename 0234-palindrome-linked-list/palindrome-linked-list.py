# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #checks out if the linked list doesn't have anything or just one 
        if not head or not head.next:
            return True 

        # find the middle node 
        fast = head 
        slow = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # reverse the linked list 
        prev = None 
        current = slow
        while current:
            next_ = current.next 
            current.next = prev 
            prev = current 
            current = next_

        # now compare them 
        first = head 
        last = prev 

        while last:# only needs to check half 
            if first.val != last.val:
                return False 
            first = first.next
            last = last.next 
        return True 