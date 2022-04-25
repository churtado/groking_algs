import pdb
"""
Given an array of sorted numbers, remove all duplicates from 
it. You should not use any extra space; after removing the 
duplicates in-place return the length of the subarray that 
has no duplicate in it.
"""
# implementation
def remove_duplicates(arr):
  e, de = 0,1
  while de < len(arr):
    if arr[e] == arr[de]:
      de += 1
      continue
    else:
      arr[e + 1] = arr[de]
      e += 1
      de +=1
  return e + 1

# examples
def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))

main()
