from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """my first attempt solution"""
        stack = []
        operations = {
            '+' : lambda x,y : x + y,
            '-' : lambda x,y : x - y,
            '/' : lambda x,y : int(x / y),
            '*' : lambda x,y : x * y,
        }
        
        for t in tokens: 
            if not (t in operations): 
                stack.append(int(t))
            else: 
                operator = operations[t]
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = operator(operand1 ,operand2)
                stack.append(res)

        return stack[-1]
    

    def evalRPN(self, tokens: List[str]) -> int:
        """neetcode's solution"""
        stack = []
        
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
