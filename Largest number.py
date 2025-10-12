class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        N = list(map(str, nums))
        N.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(N)
        if result[0] == "0":
            return "0"
        return result
