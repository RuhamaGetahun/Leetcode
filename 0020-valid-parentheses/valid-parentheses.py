class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}


        for char in s:
            if char in mapping:
                # if stack is empty or
                # if the last element of stack doesn't match the mapping return false
                if not stack or stack[-1] != mapping[char]:
                    return False 
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0