class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            k, j = i + 1, i + 2
            while j < n and k < n:
                rest = nums[i] + nums[j] + nums[k]
                result.append(rest)
                k += 1
                if k >= n and j < n - 1:
                    j += 1
                    k = j + 1
                elif j >= n - 1:
                    break

        y = [abs(a - target) for a in result]
        sol = result[y.index(min(y))]
        return sol
