class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for tick in prices:
            maxP = max(maxP, tick - minBuy)
            minBuy = min(minBuy, tick)

        return maxP