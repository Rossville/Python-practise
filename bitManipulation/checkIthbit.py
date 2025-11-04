def checkIthbit(num: int, pos: int) -> bool:
    return True if num & (1<<pos) != 0 else False

def rightShift_checkIthBit(num: int, pos: int) -> bool:
    return True if (num >> pos) & 1 == 1 else False

def printMsg(num:int, pos:int) -> None:
    msg: str = f"{pos} is set bit" if checkIthbit(num,pos) else f"{pos} is not a set bit"
    print(msg)

def main():
    num = int(input("Enter a number to check ith bit "))
    pos = int(input("Enter the ith position to check ith bit "))
    ithSetBit: bool = rightShift_checkIthBit(num, pos)
    print(ithSetBit)
    
    
if __name__ == "__main__":
    main()
    