from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """my memoization solution. Not very efficient(I beats around 10% on leetcode)"""
        self.cache = {0:0}
        
        def dfs(amount):

            if amount in self.cache:
                return self.cache[amount]
            if amount < 0: 
                return float('+inf')

            min_coins = float('+inf')
            for c in coins:
                r = amount - c 
                if r >= 0:
                    min_coins = min(dfs(r), min_coins)
            self.cache[amount] = min_coins + 1
            return min_coins + 1

        res =  dfs(amount)
        return res if res!= float('+inf') else -1


    def coinChange(self, coins: List[int], amount: int) -> int:
        """my dp solution. The efficieny is great. It consistently beats 95%> on leetcode"""
        dp = [0] * (amount + 1)

        for i in range(1,amount+1):
            res = []
            for c in coins:
                r = i - c
                if r == 0:
                    dp[i] = 1
                    break
                elif r > 0:
                    res.append(dp[r])
            else:
                dp[i] = min(res) + 1 if res else float('+inf') 
        
        return dp[-1] if dp[-1] != float('+inf') else -1
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """neetcode's dp solution."""
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
