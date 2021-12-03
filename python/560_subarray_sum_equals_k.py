class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        total = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            check = current_sum - k
            
            if check in prefix_sums:
                total += prefix_sums[check]
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
        
        return total