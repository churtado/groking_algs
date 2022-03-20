"""
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.
"""
# implementation
def max_sub_array_of_size_k(k, nums):
    m, end, s = 0, 0, 0
    while end < len(nums):
        s+=nums[end]
        if end >= k:
            s-=nums[end-k]
        end+=1
        if s>m:
            m=s
    return m

# examples
def main():
  print("Maximum sum of a subarray of size K: " +
  str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + 
   str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()
