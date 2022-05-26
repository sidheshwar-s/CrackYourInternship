class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def recurse(inventory, index):
            if index >= N: return 0
            if (inventory, index) in lookup: return lookup[(inventory, index)]
            if not inventory:
                buy = -prices[index]+recurse(True, index+1)
                not_buy = recurse(False, index+1)
                ans = max(buy, not_buy)
            else:
                sell = prices[index]+recurse(False, index+1)
                not_sell = recurse(True, index+1)
                ans = max(sell, not_sell)
            lookup[(inventory, index)] = ans
            return ans
        
        N = len(prices)
        lookup = {}
        return recurse(False, 0)