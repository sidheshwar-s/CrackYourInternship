class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, N, ans = 0, 1, len(prices), 0
        
        while right < N:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                ans = max(profit, ans)
            else:
                left = right
            right += 1
        
        return ans