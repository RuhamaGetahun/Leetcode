class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length 

        #I need a index that would hold on to the closest opening parenthesis 
        # and a stack to help me work with adding them 
        # if i end up getting an opening braket i would add it to the stack and update my index 
        # if stack and if stack[-1] is ( and the s[i] is ) substarct the i and the opening paren index 
        # 
 