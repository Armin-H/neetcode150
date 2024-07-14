class Solution:
    def isValid(self, s: str) -> bool:
        """my solution"""
        if len(s) % 2 == 1: 
            return False

        stack = []
        for c in s: 
            if c == '(': 
                stack.append(')')
            elif c == '[': 
                stack.append(']')
            elif c == '{': 
                stack.append('}')
            else: 
                if not stack: 
                    return False
                elif stack[-1] == c: 
                    stack.pop()
                else: 
                    return False

        if stack: 
            return False
        else: 
            return True


    def isValid(self, s: str) -> bool:
        """neetcode's solution"""
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    