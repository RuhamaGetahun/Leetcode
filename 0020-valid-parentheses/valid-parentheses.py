class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {')': '(', '}' :'{', ']' : '['}

        for i in s: 
            if i in characters: #check if it is a closing parenthesis 
                if not stack or stack[-1] != characters[i]:
                    return False 
                stack.pop()

            else:
                stack.append(i)
        
        return len(stack) == 0 

            