class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0

        while i < j:
            tot = nums[i] + nums[j]
            if tot == k:
                count += 1
                i += 1
                j -= 1
            elif tot < k:
                i += 1
            else:
                j -= 1
        return count
