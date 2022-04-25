"""
Given a string, find the length of the longest 
substring, which has all distinct characters.
"""
# implementation
def non_repeat_substring(str1):
    start, end, m = 0,0,0
    l = {}
    while end < len(str1):
        if str1[end] not in l:
            l[str1[end]] = 0
        l[str1[end]] += 1
        while l[str1[end]] > 1:
            l[str1[start]] -= 1
            start += 1
        end += 1
        m = max(m, end - start)
    return m

# examples
def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
