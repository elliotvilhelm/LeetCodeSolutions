class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        @lru_cache(maxsize=None)
        def dfs(sum_val, idx, values):
            if sum_val == 0:
                return True
            if sum_val < 0:
                return False
            if idx < 0:
                return False
            
            result = dfs(sum_val, idx-1, values) or dfs(sum_val - values[idx], idx - 1, values)
            return result
        
        result = dfs(total_sum / 2, len(nums) - 1, tuple(nums))
        return result