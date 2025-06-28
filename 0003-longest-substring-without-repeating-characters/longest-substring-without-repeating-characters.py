class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        string = set()
        max_string = 0 

        for end in range(len(s)):

            while s[end] in string:
                string.remove(s[start]) 
                start += 1
            string.add(s[end])
            max_string = max(max_string, end - start + 1)

        return max_string 

        