class Solution:
    # at each house decide to rob or not to rob
    # value = max(rob, dont rob)
    # value = max(value + rob, dont rob)
    # 
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def getBest(nums, index, best):
            if index >= len(nums):
                return best
            
            else:
                return max(getBest(nums, index+2, best + nums[index]), getBest(nums, index+1, best))
       
        return getBest(tuple(nums), 0, 0)