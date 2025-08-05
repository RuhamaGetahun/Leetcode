# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #edge cases like 
        if not head or not head.next:
            return True 

        # get the middle 
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        # reverse the other half 
        prev = None 
        current = slow 
        while current:
            next_ = current.next 
            current.next = prev 
            prev, current = current, next_ 

        # check if it is palindrome 
        first = head 
        last = prev 
        while last:
            if first.val != last. val:
                return False 
            first = first.next 
            last = last.next 

        return True  