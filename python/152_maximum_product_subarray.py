class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        curr_max = nums[0]
        curr_min = nums[0]
        result = curr_max
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, curr_max * curr, curr_min * curr)
            curr_min = min(curr, curr_max * curr, curr_min * curr)
            curr_max = temp_max
            
            result = max(curr_max, result)
        
        return result