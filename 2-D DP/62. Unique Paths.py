class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """my first attempt solution"""
        dp = dict()
        for i in range(m):
            dp[(i,0)] = 1

        for j in range(n):
            dp[(0,j)] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[(i,j)] = dp[((i-1),j)] + dp[(i,(j-1))]

        return dp[(m-1,n-1)]
                
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """neetcode's solution. I think my is more readable."""
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
