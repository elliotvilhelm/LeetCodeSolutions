class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx):
            if idx == len(nums):
                permutations.append(nums.copy())
            
            for i in range(idx, len(nums)):
                tmp = nums[idx]
                nums[idx] = nums[i]
                nums[i] = tmp
                
                backtrack(idx+1)
                
                tmp = nums[idx]
                nums[idx] = nums[i]
                nums[i] = tmp
         
        permutations = []
        backtrack(0)
        return permutations