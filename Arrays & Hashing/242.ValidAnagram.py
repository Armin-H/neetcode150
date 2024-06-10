from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #neetcode also mentioned this solution
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        #this is needcode's solution but I improved it using defaultdict instead of ordinary dictionaries
        #the time and space complexity of this solution is the same as the previous approach using Counter
        if len(s) != len(t): 
            return False
        
        countS, countT = defaultdict(int) , defaultdict(int)

        for i in range(len(s)): 
            countS[s[i]] += 1
            countT[t[i]] += 1

        for c in countS: 
            if countS[c] != countT[c]:
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        #the time complexity of this approach is worst than the previous approaches
        #But apparently the space complexity is better because sorting algorithms usually use O(n) extra space
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        chardict = defaultdict(int)

        for c in s:
            chardict[c] += 1
        
        for c in t:
            if c in chardict : 
                if chardict[c] == 1:
                    del chardict[c]
                else: 
                    chardict[c] -= 1
            else: 
                return False
        if len(chardict) == 0 : 
            return True