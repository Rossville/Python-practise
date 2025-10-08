from typing import List

tempNames: List[str] = ["Shubham","Amit","Abhinav","Vaibhav","Tushar","Krishna","Sumit","Ashutosh"]

def ListComprehension(rawNames: List[str]):
    names: List[str] = NamesWithAtleast3Vowels(rawNames)
    print(names)
    
def NamesWithAtleast3Vowels(names: List[str] = tempNames) -> List[str]:
    # problem statement - given list of names return only those names who have count of vowels > 2
    return [name for name in names if sum(ch in "AEIOUaeiou" for ch in name) > 2 ]
    
def get_input() -> List[str]:
    names: List[str] = []
    size: int = int(input("Enter the size of the list."))
    print(f"Enter {size} names.")
    while size != 0:
        names.append(input())
        size -= 1
    return names
    
    
def main():
    names: List[str] = get_input()
    ListComprehension(names)
    
if __name__ == "__main__":
    main()