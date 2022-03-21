"""
Given an array of positive numbers and a positive number 
‘S,’ find the length of the smallest contiguous subarray 
whose sum is greater than or equal to ‘S’. Return 0 if 
no such subarray exists.
"""
# implementation
def smallest_subarray_sum(s, arr):
    m = len(arr)+1
    sum, end, size = 0,0,0
    while end < len(arr):
        sum += arr[end]
        size += 1
        if sum >= s:
            m = min(size, s)
            while size > 1:
                sum -= arr[end-size-1]
                size -= 1
                if sum < s:
                    break
        end += 1
    if size > len(arr):
        return 0
    return size

# examples
def main():
    print("Smallest subarray length: (ex 2)" 
    + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: (ex 1)" 
    + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: (ex 3)" 
    + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))

main()
