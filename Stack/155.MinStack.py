class MinStack:
    """my solution. used the leetcode's hint to solve this."""
    def __init__(self):
        self.stack = []
        self.minToHere = []

    def push(self, val: int) -> None:
        if not self.stack: 
            self.minToHere.append(val)
        else: 
            self.minToHere.append(min(val,self.minToHere[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minToHere.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minToHere[-1]

class MinStack:
    """neetcode's solution"""
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
