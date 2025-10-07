class Solution:
    def similarPairs(self, words: List[str]) -> int:
        Y = [set(x) for x in words]
        count = 0
        for i in range(len(Y)):
            for j in range(i + 1, len(Y)):
                if Y[i] == Y[j]:
                    count += 1
        return count

