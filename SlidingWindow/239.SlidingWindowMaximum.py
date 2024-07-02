from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """my inefficient solution(TLE error on leetcode.com). time complexity: O(kn)"""
        result = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            result.append(max(window))

        return result
    

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """my efficient solution. time complexity : O(n).
        During initialization i'm initializing the deque for the first window and add the maximum of the first window to the result list.
        Neetcode's solution is also very similar to mine. but i'm recording the index in the deque but he was using 
        a left pointer to keep track of when a max digit goes out of window.
        TO DO : how do I combine initialization and iteration logica to make the code shorter."""
        
        #initializaion
        q  = deque()
        q.append((nums[0],0))
    
        for i in range(1,k):
            while q and nums[i] > q[-1][0]:
                q.pop()
            q.append((nums[i],i))

        result = [q[0][0]]

        #iterations
        for i in range(1,len(nums)-k+1):
            if i > q[0][1]: 
                q.popleft()

            while q and nums[i+k-1] > q[-1][0]: 
                q.pop()
            q.append((nums[i+k-1],i+k-1))
            
            result.append(q[0][0])

        return result
    

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        "neetcode's solution"
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
