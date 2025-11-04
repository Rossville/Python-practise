from typing import Tuple, List

def MaximumSubarrayIterative(ls: List[int]) -> Tuple[int,int,int]:
    start_indx: int = -1
    end_indx: int = -1
    maxSum: float = float('-inf')
    list_len = len(ls)
    sum: int = 0
    for i in range(0, list_len):
        sum = ls[i]
        for j in range(i+1, list_len):
            sum += ls[j]
            print(sum)
            if sum > maxSum :
                start_indx = i
                end_indx = j
                maxSum = sum
                
    return (start_indx,end_indx,int(maxSum))


def FindMaxCrossingSum(arr: List[int], low:int, mid: int, high: int):
    left_sum: int = 0
    sum = 0
    max_left: int = -1
    for i in range(mid, low, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum: int = 0
    max_right: int = -1
    for i in range(mid+1, high):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return (max_left, max_right, int(left_sum + right_sum))

def MaximumSubarrayRecursive(arr: List[int], low:int , high: int) -> Tuple[int,int,int]:
    if low == high:
        return (low, high, arr[low])
    else:
        left_low: int
        left_high: int
        left_sum: int
        right_low: int
        right_high: int
        right_sum: int
        cross_low: int
        cross_high: int
        cross_sum: int
        mid = (low+high)//2
        (left_low, left_high, left_sum) = MaximumSubarrayRecursive(arr, low, mid)
        (right_low, right_high, right_sum) = MaximumSubarrayRecursive(arr, mid+1, high)
        (cross_low, cross_high, cross_sum) = FindMaxCrossingSum(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high ,right_sum)
        return (cross_low, cross_high, cross_sum)
        
        
def main():
    n: int = int(input("Enter the size of list:\n"))
    ls: List[int] = []
    for _ in range(n):
        ls.append(int(input("Enter an element:\n")))
    tp: Tuple[int,int,int]
    # tp = MaximumSubarrayIterative(ls)
    tp = MaximumSubarrayRecursive(ls, 0, len(ls)-1)
    print(tp)
    
if __name__ == "__main__":
    main()
    