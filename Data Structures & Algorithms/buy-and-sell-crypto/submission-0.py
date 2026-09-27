class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_buy = prices[0]
        profit = 0
        for i in prices:
            if i < min_buy:
                min_buy = i
            profit = max(profit, i-min_buy)
        return profit


        
        