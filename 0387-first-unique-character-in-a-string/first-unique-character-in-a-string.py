class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}

        for i in range(len(s)):
            store[s[i]] = store.get(s[i], 0) + 1 

        for i , letter in enumerate(s):
            if store[letter] == 1:
                return i 
        
        return -1 

        