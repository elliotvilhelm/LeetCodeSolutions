class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for idx, i in enumerate(nums):
            c = target - nums[idx]
            if c in index_map and index_map[c] != idx:
                return [index_map[c], idx]
            index_map[i] = idx