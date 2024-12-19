class Solution:
    def hammingWeight(self, n: int) -> int:
        """my first attempt solution, same as neetcode's first solution, he used while(n) instead of the for loop"""
        res = 0
        for _ in range(32):
            res += n & 1
            n = n >> 1
        return res
    
     
    def hammingWeight(self, n: int) -> int:
        """neetcode's second solution"""
        res = 0
        while n:
            n &= (n-1)
            res += 1

        return res