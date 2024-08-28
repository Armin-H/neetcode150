from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """my first attempt solution. Time complexity is O(n), Space complexity is O(n).
        Neetcode's solution is better because he is using constant space complexity by using the input array itself."""
        DP = [0] * len(cost)
        DP[-1] = cost[-1]
        DP[-2] = cost[-2]

        for i in range(len(cost)-3,-1,-1): 
            DP[i] = cost[i] + min(DP[i+1] , DP[i+2])

        return min(DP[0],DP[1])
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """neetcode's solution"""
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
