"""
Given an array of positive numbers and a positive number 
‘S,’ find the length of the smallest contiguous subarray 
whose sum is greater than or equal to ‘S’. Return 0 if 
no such subarray exists.
"""
import math

# implementation
def smallest_subarray_sum(s, arr):
    m = math.inf
    start, end, sum = 0,0,0
    while end < len(arr):
        sum += arr[end]
        end += 1
        while sum >= s:
            m = min(m, end - start)
            sum -= arr[start]
            start += 1
    if m == math.inf:
        return 0
    return m

# examples
def main():
    arr = [2, 1, 5, 2, 3, 2]
    print(f"Smallest subarray length: (ex 2) {smallest_subarray_sum(7, arr)}")
    arr = [3, 4, 1, 1, 6]
    print(f"Smallest subarray length: (ex 2) {smallest_subarray_sum(7, arr)}")
    arr = [2, 1, 5, 2, 8]
    print(f"Smallest subarray length: (ex 1) {smallest_subarray_sum(7, arr)}")

main()
