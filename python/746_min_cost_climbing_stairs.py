class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[1]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        dp = [0] * (len(cost)+1)
        
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        print(dp)
        return dp[-1]