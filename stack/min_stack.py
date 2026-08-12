import sys

class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
        self.min_value = sys.maxsize

    def push(self, val: int) -> None:
        self.min_value = min(self.min_value, val)
        self.mins.append(self.min_value)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()
        minpop = self.mins.pop()
        if len(self.mins) == 0:
            self.min_value = sys.maxsize
        elif minpop != self.mins[-1]:
            self.min_value = self.mins[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
