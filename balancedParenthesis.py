# 1. [{} ()]        (Y)
# 2. (){}[]         (Y)
# 3. {{()}}{}[]     (Y)
# 4. [( {}]         (N)
# 5. ([{])          (N)

from stackImplementationUsingArray import Mystack
from typing import List


parenthesis_map = {
    '[': ']',
    '{': '}',
    '(': ')'
}

def balanced_parenthesis(s: str):
    newStack = Mystack()    # initialization
    for i in s:
        if i == '[' or i == '{' or i == '(':
            newStack.push(i)
        else:
            if newStack.empty():
                return False
            if parenthesis_map[newStack.top()] != i:
                return False
            newStack.pop()
            
    return newStack.empty()
            

def main() -> None:
    s: List[str] = ['[{}()]', '(){}[]', '{{()}}{}[]', '[({}]', '([{])']
    for i in s:
        if balanced_parenthesis(i):
            print(f"{i} \t\t [Balanced Parenthesis]")
        else:
            print(f"{i} \t\t [Unbalanced Parenthesis]")
    
        
if __name__ == "__main__":
    main()
    