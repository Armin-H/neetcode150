from typing import List
import collections

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """my first attempt dp solution. it passes leetcode's test but it's inefficient(beats around 7%).
        I think it's because I'm filling the entire dp table, but we might not need to.
        Because to fill out the dp[len(coins)-1][amount] which is the solution we only need the previous row.
        So filling out the last row is actually not nececarry. For instance if amount = 301 and the value of the last coin is 100,
        then we only need few values from the previous row(3 to be exact, but in the current code we are filling 301 cells instead of 3).
        So I think a recursive memoization solution would be better.(but i'm not sure)"""
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

        for j in range(amount+1):
            dp[0][j] = 1 if j % coins[0] == 0 else 0 

        for i in range(len(coins)):
            dp[i][0] = 1

        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                n = 0
                while True:
                    r = j - n*coins[i]

                    if r > 0:
                        dp[i][j] += dp[i-1][r]
                        n += 1
                    elif r == 0:
                        dp[i][j] += 1
                        break
                    else:
                        break

        return dp[len(coins)-1][amount]
                    
                
    def change(self, amount: int, coins: List[int]) -> int:
        """my recursive memoization solution. Still not very efficent beats around 10%,
        I think the inefficiency may be due to the excessive recursive calls, so eventhough a value 
        might already be in cash the function is still called for that(although I'm not sure)"""
        self.cache = collections.defaultdict(int)
        for j in range(amount+1):
            self.cache[(0,j)] = 1 if j % coins[0] == 0 else 0 

        for i in range(len(coins)):
            self.cache[(i,0)] = 1

        def dfs(i,amount):

            if (i,amount) in self.cache:
                return self.cache[(i,amount)]

            n = 0
            while True:
                r = amount - n*coins[i]
                if r == 0:
                    self.cache[(i,amount)] += 1
                    break
                elif r > 0:
                    self.cache[(i,amount)] += dfs(i-1,r)
                    n += 1
                else:
                    break
            return self.cache[(i,amount)]

        return dfs(len(coins)-1,amount)


    def change(self, amount: int, coins: List[int]) -> int:
        """neetcode's dp solution. The space complexity of this solution is O(amount) instead of O(amount*len(coins) in my solution."""
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
