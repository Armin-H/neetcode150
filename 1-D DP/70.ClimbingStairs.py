class Solution:
    def climbStairs(self, n: int) -> int:
        """recusive solution. Time complexity is O(2^n)"""
        if n <= 2: 
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n: int) -> int:
        """my bottom-up DP solution. Time complexity is O(n), Space Complexity is O(n).
        The solution below is better because of constance space complexity."""
        if n <= 2:
            return n

        num_steps = [1,2]
        
        for _ in range(n-2):
            num_steps.append(num_steps[-1] + num_steps[-2])
        return num_steps[-1]
    
    def climbStairs(self, n: int) -> int:
        """my bottom-up DP solution. Time complexity is O(n), Space Complexity is O(1)"""
        if n <= 2:
            return n

        n1,n2 = 1,2

        for _ in range(n-2):
            n1,n2 = n2,n1+n2

        return n2