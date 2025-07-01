class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # iterate through nums2 and find the next greater 
        # and keep em in dictionary to make it easy to search for nums1 
        for n in nums2:

            while stack and n > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = n 

            stack.append(n)

        # after all what's left in the stack doesn't have a greater number following 
        for n in stack:
            next_greater[n] = -1

        return [next_greater[n] for n in nums1]

        