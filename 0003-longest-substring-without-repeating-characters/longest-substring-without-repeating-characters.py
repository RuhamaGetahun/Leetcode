class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        start = 0 
        max_length = 0 

        for end in range(len(s)):
            while s[end] in store:
                store.remove(s[start])
                start += 1

            store.add(s[end])
            max_length = max(max_length, end - start + 1)

        return max_length 

    
        
        