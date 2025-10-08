from typing import List

def Subarr_sum(arr: List[int], st:int, end:int) -> int:
    total:int = 0
    for i in range(st,end+1):
        total += arr[i]
    return total


def subArr(arr: List[int]) -> List[int]:
    # subarr_list: List[dict[str, int]] = [{startingIndex: ,EndingIndex: ,sum: }]
    subarr_list: List[dict[str, int]] = []
    # keeping i constant
    subarr_list = [{"startingIndex": i, "endingIndex": j, "sum": Subarr_sum(arr, i, j)} for i in range(len(arr)) for j in range(len(arr)) if i!=j]
    subarr_list.sort(key=lambda x: x["sum"])
    d: dict[str, int] = subarr_list.pop(len(subarr_list)-1)
    num: List[int] = []
    for x in range(d["startingIndex"],d["endingIndex"]+1):
        num.append(arr[x])
    return num
    
def main() -> None:
    Size:int = int(input("Enter the size of the array"))
    print("Enter the elements of the array")
    lst: List[int] = []
    for _ in range(Size):
        lst.append(int(input()))
    print(f" Maximum subarray : {subArr(lst)}")

if __name__ == "__main__":
    main()
