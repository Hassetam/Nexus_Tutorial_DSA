class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        start = 0
        max_len = 0

        for end in range(len(s)):
            while s[end] in x:
                x.remove(s[start])
                start += 1
            x.add(s[end])
            max_len = max(max_len, end - start + 1)
        
        return max_len
