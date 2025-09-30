class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = ""
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                num = int(s[i:i+2])   # e.g. "10"
                ans += chr(ord("a") + num - 1)
                i += 3
            else:
                num = int(s[i])       # e.g. "1"
                ans += chr(ord("a") + num - 1)
                i += 1
        return ans

       
