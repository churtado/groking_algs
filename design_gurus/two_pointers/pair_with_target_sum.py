import pdb
"""
Given an array of sorted numbers and a target sum, find 
a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers 
(i.e. the pair) such that they add up to the given target.
"""
# implementation
def pair_with_targetsum(arr, target):
    index = 0 
    h = {}
    while index < len(arr):
        h[arr[index]] = index
        if (target - arr[index]) in h and (target - arr[index]) != arr[index]:
            return [h[(target - arr[index])], h[arr[index]]]
        index += 1
    return []

# examples
def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))

main()
