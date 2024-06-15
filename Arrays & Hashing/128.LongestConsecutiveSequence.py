from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """my solution. very similar to neetcode's solution.
            Mine is more efficient because neetcode's solution doesn't handle duplicates"""
        numSet = set(nums)
        longest = 0 
        while numSet:
            n = numSet.pop()
             
            if n-1 in numSet: 
                numSet.add(n)
            else:
                currlen = 1
                while n+ currlen in numSet:
                    numSet.remove(n+currlen)
                    currlen += 1
                longest = max(longest, currlen)
        return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        """neetcode's solution"""
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
