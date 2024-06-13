from collections import Counter, defaultdict
from typing import List

class Solution:
    """general idea: create a representation for each group  and store it as key in a dictionary 
    ,  values corresponding to each key is list of anagrams for matching the key.
    simplest representation: sorted version of each anagram
        time complexity using this: O(mnlog(n))  --> m: len(strs), n: length of each string
    better solution is to use a hashmap(e.g. python Couter object) as representation of a group
        time complexity: O(mn)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #my first attempt solution(not efficient)
        anagrams = defaultdict(list)

        for s in strs:
            anagrams[tuple(sorted(tuple(Counter(s).items()), key = lambda x : x[0]))].append(s)
        return list(anagrams.values())
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #neetcode's solution
        result = defaultdict(list)

        for s in strs: 
            count = [0] * 26
            for c in s: 
                count[ord(c)-ord('a')] += 1
            #lists are not hashable 
            result[tuple(count)].append(s)

        return result.values()