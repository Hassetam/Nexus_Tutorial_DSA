class Solution:
    def commonFactors(self, a: int, b: int) -> int:
            x = [n for n in range(1, a + 1) if a % n == 0]
            y = [m for m in range(1, b + 1) if b % m == 0]
            return len(set(x) & set(y))
