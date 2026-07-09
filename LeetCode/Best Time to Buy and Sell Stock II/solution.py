from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        totalProfit=0
        
        for i in range(1, len(prices), 1):
            if prices[i]>prices[i-1]:
                totalProfit += prices[i] - prices[i-1]
        
        return totalProfit