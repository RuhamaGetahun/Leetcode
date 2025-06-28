class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

         # iterate through s and append it to the stack 
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else: # until we find a closing bracket 

                # then pop the previous string until opening bracket and add it to be a string 
                char = ""
                while stack[-1] != '[':
                    char = stack.pop()+ char 
                stack.pop() # then pop the opening braket 

                key = ""
                while stack and stack[-1].isdigit():
                    key = stack.pop() + key 
                
                stack.append(int(key) * char )  # multiply the string by the number and append back to the stack 

        return "".join(stack)


            
