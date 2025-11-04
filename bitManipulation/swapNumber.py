# from collections import tuple

def swapNum(a:int, b:int):
    a = a^b
    b = a^b
    a = a^b
    return (a,b)

def main() -> None:
    a = int(input("Enter num1"))
    b = int(input("Enter num2"))
    x = swapNum(a,b)
    print(f"Swapped the two given numbers: {a} and {b} which becomes {x[0], x[1]}")
    
if __name__ == "__main__":
    main()