"""
Given an array of unsorted numbers, 
find all unique triplets in it that add up to zero.
"""
# implementation
def search_triplets(arr):
  arr.sort()
  t = []
  i = 0
  while i < len(arr):
    if i > 0 and arr[i-1] == arr[i]:
      i += 1
      continue
    search_pairs(arr, i, t)
    i += 1
  return t

def search_pairs(arr, index, t):
  target = -arr[index]
  left = index + 1
  right = len(arr) - 1
  while left < right:
    if arr[left] + arr[right] == target:
      t.append([arr[index], arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left-1]:
        left += 1
      while left < right and arr[right] == arr[right+1]:
        right -= 1
    elif target > arr[left] + arr[right]:
      left += 1
    else:
      right -= 1

# examples
def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))

main()
