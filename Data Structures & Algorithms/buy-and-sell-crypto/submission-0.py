class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = prices[0]
        max_val = 0
        hpro = 0

        for price in prices:

            if price < min_val:
                min_val = price
                max_val = price
            
            if price > max_val:
                hpro = max(hpro,price-min_val)
                max_val = price
        return hpro


        