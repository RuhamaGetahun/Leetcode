# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None 

        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy 
        while heap:
            val, indx, node = heapq.heappop(heap)
            current.next = node 
            current = node  
            node = node.next 

            if node:
                heapq.heappush(heap, (node.val, indx, node))

        return dummy.next 