class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                pf = prices[j] - prices[i]
                if pf > profit:
                    profit = pf

        return profit


