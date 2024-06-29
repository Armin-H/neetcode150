from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """greedy solution. Time complexity: O(n^2)"""
        maxP = 0

        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                currProfit = prices[j] - prices[i]
                maxP = max(currProfit, maxP)

        return maxP
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """my solution. time complexity: O(n), space complexity : O(1)
        neetcode's solution is also the same"""
        maxP = 0
        l,r = 0,1
        while r <= len(prices)-1:
            if prices[l] < prices[r]: 
                maxP = max(maxP, prices[r] - prices[l])
                r += 1
            else: 
                l = r
                r += 1
        return maxP