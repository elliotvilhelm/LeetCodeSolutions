class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = [0] * len(prices)
        for i in range(1, len(prices)):
            max_p[i] = max(max_p[i-1], max_p[i-1] + prices[i] - prices[i-1])
        return max_p[-1]