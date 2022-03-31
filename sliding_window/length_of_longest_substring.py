"""
Given a string with lowercase letters only, if you are 
allowed to replace no more than ‘k’ letters with any 
letter, find the length of the longest substring having 
the same letters after replacement.
"""
# implementation
def length_of_longest_substring(str1, k):
    start, end, m, mc = 0,0,0,0
    h = {}
    while end < len(str1):
        if str1[end] not in h:
            h[str1[end]] = 0
        h[str1[end]] += 1
        mc = max(mc, h[str1[end]])
        while end - start + 1 - mc > k:
            h[str1[start]] -= 1
            start += 1
        end += 1
        m = max(m , end - start)
    return m

# examples
def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))

main()
