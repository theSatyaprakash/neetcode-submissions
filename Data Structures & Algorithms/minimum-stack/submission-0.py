class MinStack:

    def __init__(self):
        self.l=[]
        self.s=[]

    def push(self, val: int) -> None:
        self.l.append(val)
        val=min(val,self.s[-1] if self.s else val)
        self.s.append(val)
    def pop(self) -> None:
        self.l.pop()
        self.s.pop()
    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.s[-1]

        
