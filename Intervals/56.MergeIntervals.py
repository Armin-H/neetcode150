from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """my first attempt solution. My solution is very similar to 57"""
        sorted_intervals = sorted(intervals, key = lambda x : x[0])

        res = []
        curr_interval = None
        for interval in sorted_intervals:
            if not curr_interval:
                curr_interval = interval
            else:
                if interval[0] > curr_interval[1]:
                    res.append(curr_interval)
                    curr_interval = interval
                else:
                    curr_interval = [min(curr_interval[0],interval[0]),
                                     max(curr_interval[1],interval[1])]
        
        res.append(curr_interval)
        return res
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """neetcode's solution"""
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
