class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        had = sum(int(d) for d in str(x))
        return had if x % had == 0 else -1
