from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """my first attempt solution, although it passes the leetcode test, it's not efficient.
        The time complexity is O(nlogn), but it could be done in O(nlogk)"""
        class Point:
            
            def __init__(self,x,y):
                self.x = x
                self.y = y
            def distance_to_origin(self):
                return self.x ** 2 + self.y **2

            def __lt__(self,other):
                return self.distance_to_origin() < other.distance_to_origin()

            def get_coords(self):
                return [self.x,self.y]

        minheap = []
        for p in points:
            p = Point(*p)
            heapq.heappush(minheap, p)

        return [heapq.heappop(minheap).get_coords() for i in range(k)]
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """neetcode's solution. Time complexity is O(nlogk)"""
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res
