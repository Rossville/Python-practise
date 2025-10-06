# from typing import Any
def pattern1(row: int) -> None:
    # x:int = 2
    temp:int = 0
    for i in range(row):
        temp += i+1
        for j in range(temp, 0, -1):
            a = j+i if j%2 != 0 else "*"
            print(a,sep=" ",end="")
        print()
        temp += 1

def hollowInvertedHalfPyramid(row: int) -> None:
    # ls: list[list[Any]] = [[]]
    for i in range(row):
        for j in range(row):
            if i == 0 or j == row-1 or (i == j and i>0 and i<row-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()


def main() -> None:
    row = int(input("Enter the row size."))
    # pattern1(row)
    hollowInvertedHalfPyramid(row)

if __name__ == "__main__":
    main()
