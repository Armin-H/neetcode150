class Solution:
    def isPalindrome(self, s: str) -> bool:
        """my solution"""
        i,j = 0,len(s)-1
        while i <= j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower() != s[j].lower(): 
                return False
            else:
                i+=1
                j-=1
        return True

    def isPalindrome(self, s: str) -> bool:
        """neetcode's solution. l and r are better naming than i and j"""
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
