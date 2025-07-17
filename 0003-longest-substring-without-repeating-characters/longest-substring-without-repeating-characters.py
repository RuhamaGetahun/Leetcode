class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       start = 0 
       store = set()
       max_length = 0 

       for i in range(len(s)):
        while s[i] in store:
            store.remove(s[start])
            start += 1 
        store.add(s[i])
        max_length = max(max_length, i - start + 1)
       return max_length 