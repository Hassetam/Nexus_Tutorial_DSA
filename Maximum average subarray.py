class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        max_sum = current_sum = sum(nums[i:j])
        while j < len(nums):
            current_sum += nums[j] - nums[i]
            max_sum = max(max_sum, current_sum)
            i += 1
            j += 1
        return max_sum / k
