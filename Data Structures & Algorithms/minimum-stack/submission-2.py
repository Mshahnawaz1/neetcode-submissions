class MinStack:

    def __init__(self):
        # last element of

        self.minstack = []
        self.data = []


    def push(self, val: int) -> None:
        self.data.append(val)

        if self.minstack:
            if val < self.minstack[-1]:
                val = val
            else:
                val = self.minstack[-1]
        else:
            val = val
        self.minstack.append(val)
        

    def pop(self) -> None:
        self.data.pop()
        self.minstack.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
