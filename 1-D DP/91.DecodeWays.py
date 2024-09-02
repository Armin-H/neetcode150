class Solution:
    def numDecodings(self, s: str) -> int:
        """my dp solution. I think the initialization of the first two elements in the dp array can be simplified.
        I think we can reduce the space complexity to constant by only using two variables instead of the whole dp array."""
        codes = [str(i) for i in range(1,27)]

        if len(s) == 1:
            return int(s in codes)

        #initialization for the first two elements
        dp = [0] * len(s)
        if s[0] in codes:
            dp[0] = 1
        else:
            return 0 
        dp[1] += 1 if s[1] in codes else 0 
        dp[1] += 1 if s[0:2] in codes else 0


        for i in range(2,len(dp)):

            dp[i] += dp[i-1] if s[i] in codes else 0
            dp[i] += dp[i-2] if s[i-1:i+1] in codes else 0

            if dp[i] == 0:
                return 0

        return dp[-1]
    
 
    def numDecodings(self, s: str) -> int:
        """Neetcode's memoization solution. dfs(i) means number of ways to decode s starting from index i,
        so dfs(0) is the answer."""
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)


    def numDecodings(self, s: str) -> int:
        """Neetcode's dynamic programming solution."""
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]
