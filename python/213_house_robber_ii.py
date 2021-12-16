class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def getBest(nums, index, best):
            if index >= len(nums):
                return best
            
            return max(getBest(nums, index+1, best), getBest(nums, index+2, best + nums[index]))
        if len(nums) == 1:
            return nums[0]
        return max(getBest(tuple(nums[1:]), 0, 0), getBest(tuple(nums[:-1]), 0, 0))