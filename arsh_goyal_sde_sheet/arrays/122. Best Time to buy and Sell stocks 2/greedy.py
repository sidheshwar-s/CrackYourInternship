class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices) - 1
        profit = 0
        i = 0
        while i < N:
            while i < N and prices[i+1] <= prices[i]: 
                i += 1
            buy = prices[i]
            
            while i < N and prices[i+1] > prices[i]:
                i += 1
            sell = prices[i]
            profit += sell - buy
        
        return profit
            