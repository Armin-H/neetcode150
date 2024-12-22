from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        """my first attempt dp solution, this solution was marked as optimal in neetcode's website(5th sol).
        there are 5 solutions here: https://neetcode.io/problems/counting-bits"""
        res = [0, 1, 1]
        for i in range(3,n+1):
            res.append((i & 1) + res[i >> 1])

        return res[:n+1]

