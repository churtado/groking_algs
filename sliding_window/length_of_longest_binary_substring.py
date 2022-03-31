"""
Given an array containing 0s and 1s, if you are 
allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.
"""
# implementation
def length_of_longest_substring(arr, k):
    start, end, m, zc = 0,0,0,0
    while end < len(arr):
        if arr[end] == 0:
            zc += 1
        while zc > k:
            if arr[start] == 0:
                zc -= 1
            start += 1
        end += 1
    if m < end - start:
        m = end - start
    return m

# examples
def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()
