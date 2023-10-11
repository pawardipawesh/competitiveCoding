class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        # for i in range(0, len(prices)-1):
        #     candidate_profit = max(prices[i+1:]) - prices[i]
        #     if candidate_profit >  profit:
        #         profit = candidate_profit

        buy = prices[0]
        for i in range(1, len(prices)):
            cp = prices[i]
            curr_profit = cp - buy
            if curr_profit > profit:
                profit = curr_profit
                continue
            
            if cp < buy:
                buy = cp

        return profit
