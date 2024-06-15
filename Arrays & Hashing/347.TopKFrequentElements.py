from typing import List
from collections import Counter,defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k[0] for k in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #neetcode's solution but using defaultdict instead of normal dict
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for n,c in counts.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]: 
                if len(result) < k: 
                    result.append(n)

        return result