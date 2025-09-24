class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = strs[0]
        for s in strs[1:]:
            while not s.startswith(x):
                x = x[:-1]
                if not x:
                    return ""
        return x
