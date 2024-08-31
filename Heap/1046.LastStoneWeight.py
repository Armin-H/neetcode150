import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """my first attempt solution."""
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        
        while len(maxheap) >= 2:
            s1 = heapq.heappop(maxheap)
            s2 = heapq.heappop(maxheap)
            if s1 < s2:
                heapq.heappush(maxheap, s1-s2)
            
        if len(maxheap) == 0:
            return 0
        else:
            return -maxheap[0]
        
    def lastStoneWeight(self, stones: List[int]) -> int:
        """neetcode's solution. Identical strategy as mine."""
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
