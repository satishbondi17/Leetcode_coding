class Solution(object):
    def maxProfit(self, prices):
        max_pro = 0
        min_price=float("inf")
        for i in range(0,len(prices)):
           min_price=min(min_price,prices[i])
           max_pro=max(max_pro,prices[i]-min_price)
        return max_pro

        