class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 9999999
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit