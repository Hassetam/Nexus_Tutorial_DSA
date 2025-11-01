class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        i = 0
        n = i + len(p)

        P = Counter(p)
        while n <= len(s):
            x = s[i:n]
            X = Counter(x)

            if P == X:
                result.append(i)
            i += 1
            n += 1

        return result
