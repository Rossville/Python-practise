def checkOdd(num: int) -> bool:
    val:bool = True if num %2 != 0 else False
    return val

def main():
    num:int = int(input("Enter a number"))
    if(not checkOdd(num)):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

main()