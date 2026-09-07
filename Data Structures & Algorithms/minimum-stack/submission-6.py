class MinStack:

    def __init__(self):
        self.stk = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        cmin = min(val, self.mini[-1]) if self.mini else val
        self.mini.append(cmin)

    def pop(self) -> None:            
        out = self.stk.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
