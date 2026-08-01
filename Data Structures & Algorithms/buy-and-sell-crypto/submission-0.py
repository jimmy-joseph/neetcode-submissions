class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0

        low = prices[0]
        high = prices[0]
        
        for i, n in enumerate(prices):
            if low > prices[i]:
                low = prices[i]
                high = prices[i]
            if high < prices[i]:
                high = prices[i]

            if high - low > max:
                print(high)
                print(low)
                max = high - low

        return max