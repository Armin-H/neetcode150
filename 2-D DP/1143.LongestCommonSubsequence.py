import collections

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """my recursive solution. I think this is correct, but leetcode gives me TLE"""        
        m = len(text1)
        n = len(text2)
        
        if m == 0 or n == 0:    
            return 0

        if text1[-1] == text2[-1]:
            return 1 + self.longestCommonSubsequence(text1[:-1],text2[:-1])
        else:
            return max(self.longestCommonSubsequence(text1,text2[:-1]),
                        self.longestCommonSubsequence(text1[:-1],text2))
        

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """my first attempt DP solution. Although it passes leetcode's test it's inefficient(beats around 10%).
        I think it's because I'm filling out the entire dp table, but in some cases we don't need to do so.
        For instance if last character of text1 and text2 are the same then we don't need any values in the last row and the last column,
        but here we are computing all of them no matter what."""
        m = len(text1)
        n = len(text2)
        
        dp = collections.defaultdict(int)

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[(i,j)] = dp[(i-1,j-1)] + 1
                else:
                    dp[(i,j)] = max(dp[(i,j-1)],dp[(i-1,j)])

        return dp[i,j]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """neetcode's solution. This is beating around 60% on leetcode.
        I think this is the same approach as mine(it fills out the entire dp table first),
        So I don't know why this is faster than mine."""
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
