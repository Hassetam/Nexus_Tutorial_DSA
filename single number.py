class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x =nums[i]
            y =nums[i+1:]
            if x in y:
                continue
            elif x in nums[:i]:
                continue
            else:
                return x
                
