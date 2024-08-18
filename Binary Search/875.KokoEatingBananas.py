from typing import List
import math
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """my bruteforce solution(TLE error on leetcode)"""
        eating_rate = 1
        while True: 
            total_hour_needed = sum([ceil(p / eating_rate) for p in piles])
            if total_hour_needed >h: 
                eating_rate += 1
            else: 
                return eating_rate

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """my binary-serach solution."""
        from math import ceil
        l,r = 1, max(piles)
        curr_best = r
        while l <= r: 
            eating_rate = (l + r) // 2
            total_hour_needed = sum(ceil(p / eating_rate) for p in piles)
            if total_hour_needed > h: 
                l = eating_rate + 1
            elif total_hour_needed <= h:
                r = eating_rate - 1
                curr_best = eating_rate

        return curr_best
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """neetcode's solution"""
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
