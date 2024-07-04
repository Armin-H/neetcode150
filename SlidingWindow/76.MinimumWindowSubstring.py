from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """my messy, inefficient, first attempt solution. Although it passes all the tests on leetcode,
        it only beats around 5% of other solution."""
        if len(s) < len(t): 
            return ""

        tCount = defaultdict(int) 
        for i in range(len(t)): 
            tCount[t[i]] += 1

        #set left 
        l = 0 
        while l <= len(s) - 1 :
            if s[l] not in tCount: 
                l += 1
            else:
                break
        else: 
            return ""

        have = {k: 0 for k in tCount}
        have[s[l]] += 1

        if have == tCount: 
            return s[l]

        best = None
        r = l 
        while r < len(s)-1:  
            r += 1
            if s[r] in tCount:
                have[s[r]] += 1

            if all(have[k] >= tCount[k] for k in tCount):
                while all(have[k] >= tCount[k] for k in tCount):
                    if s[l] in tCount: 
                        have[s[l]] -= 1
                    l += 1

                l -= 1
                if s[l] in tCount: 
                    have[s[l]] += 1
                if best is None or r-l < best[1]-best[0]: 
                    best = (l,r)

        if best: 
            return s[best[0]:best[1]+1]
        else:
            return ""
            