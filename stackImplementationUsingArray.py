from typing import List

class Mystack:
    def __init__ (self):
        self.arr: List[str] = []
    
    def push(self, val: str):
        self.arr.append(val)
    
    def pop(self) -> str:
        if len(self.arr) == 0:
            print("Cannot use pop() on the empty List")
            return ""
        return self.arr.pop()
    
    def top(self) -> str:
        return self.arr[-1]        
    
    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False
    
    def size(self) -> int:
        return len(self.arr)
    
    def print(self):
        print(self.arr)
    

newStack = Mystack() #initialization


# newStack.push(2)
# newStack.push(4)
# newStack.push(5)
# newStack.push(7)
# newStack.push(9)

# newStack.print()

# newStack.pop()
# newStack.pop()
# newStack.pop()

# newStack.print()

# print(f"Size : {newStack.size()}")


        
