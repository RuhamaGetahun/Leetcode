class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        store = {}
        max_length = 0 

        for end in range(len(s)):
            store[s[end]] = store.get(s[end], 0) + 1 

            while store[s[end]] > 1:
                store[s[start]] -= 1 
                if store[s[start]] == 0:
                    del store[s[start]]
                start += 1 
            max_length = max(max_length, end - start + 1)
        return max_length 