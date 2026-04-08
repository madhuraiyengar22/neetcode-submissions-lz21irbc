class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price_ind = 0
        sell_price_ind = 1
        l = 0
        r = 1
        maxprofit = 0
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > maxprofit:
                    maxprofit = profit
            else:
                l = r
            r += 1
        return maxprofit
        