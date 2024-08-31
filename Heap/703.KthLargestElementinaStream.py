from typing  import List
import heapq

class KthLargest:
    """neetcode's solution. I think this can be improved,
    because hse is creating the heap with all the elements and the removing until k elements are left.
    We can just start pushing to the heap and limit the size to k."""
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
