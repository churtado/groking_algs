"""
Given a sorted array, create a new array containing 
squares of all the numbers of the input array in the sorted order.
"""
# implementation
def make_squares(arr):
  n,p = 0,0
  arr2 = []
  # find first non-negative number
  while arr[p] < 0:
    p += 1
  n = p - 1
  while len(arr2) < len(arr):
    if n < 0  and p == len(arr):
      break
    if n < 0:
      arr2.append(arr[p]**2)
      p += 1
      continue
    if p == len(arr):
      arr2.append(arr[n]**2)
      n -= 1
      continue
    if arr[n]**2 <= arr[p]**2:
      arr2.append(arr[n]**2)
      n -= 1
      continue
    if arr[p]**2 < arr[n]**2:
      arr2.append(arr[p]**2)
      p += 1
      continue
  return arr2

# examples
def main():
  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))

main()
