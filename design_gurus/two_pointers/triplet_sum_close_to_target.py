"""
Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the 
target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum 
of the triplet with the smallest sum.
"""
import math
# implementation
def triplet_sum_close_to_target(arr, target_sum):
  # sort the array
  arr.sort()

  min_difference = math.inf

  for i in range(len(arr) - 2):
    # for every number, calculate it's sum with the 2 others
    # a + b + c = target -> b + c = target - a
    j,k = i+1, len(arr) - 1
    while j < k:
      current_diff = target_sum - (arr[i] + arr[j] + arr[k])
      if current_diff == 0:
        return target_sum

      # fucking hard condition right here 
      if abs(current_diff) < abs(min_difference) or \
        (abs(current_diff) == abs(min_difference) and current_diff > min_difference):
        min_difference = current_diff

      if current_diff > 0:
        j += 1
      else:
        k -= 1
    # if the sum is close to target, save the sum
  return target_sum - min_difference

# examples
def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))

main()
