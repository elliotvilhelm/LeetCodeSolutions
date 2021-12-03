class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        best_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            best_max = max(current_max, best_max)
        
        return best_max