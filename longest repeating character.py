class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        n = len(s)
        max_len = 0
        count = {}

        while j < n:
            count[s[j]] = count.get(s[j], 0) + 1

            # if too many replacements are needed
            while (j - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len
