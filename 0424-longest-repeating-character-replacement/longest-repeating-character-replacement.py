class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        state = {}
        start = 0 
        max_freq = 0 
        max_length = 0 

        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1 
            max_freq = max(max_freq, state[s[end]])

            while k + max_freq < end - start + 1: #!!!! 
                state[s[start]] -= 1 
                if state[s[start]] == 0:
                    del state[s[start]]
                start += 1

            max_length = max(max_length, end - start + 1)
        return max_length  
        