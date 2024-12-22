from collections import deque
class Solution:
    def reverseBits(self, n: int) -> int:
        """my first attempt solution. Having the deque is not necessary."""
        
        q = deque(maxlen=32)
        for _ in range(32):
            q.append(n & 1)
            n = n >> 1
        res = 0
        for _ in range(32):
            res += q.popleft()
            res = res << 1
        return res >> 1

    def reverseBits(self, n: int) -> int:
        """neetcode's video solution, it doesn't seem very time efficient """
        res = 0

        for i in range(32):
            bit = 1 & (n >> i)
            res += bit << (31-i) # |= can also be used instead of +=

        return res
    