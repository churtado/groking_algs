"""
Given a string, find the length of the longest substring
in it with no more than K distinct characters.
You can assume that K is less than or equal to the length
of the given string.
"""
# implementation
def longest_substring_with_k_distinct(s, k):
    start, end, m = 0,0,0
    letters = {}
    while end < len(s):
        if s[end] not in letters:
            letters[s[end]] = 0
        letters[s[end]] += 1
        end += 1
        while  len(letters) > k:
            letters[s[start]] -= 1
            if letters[s[start]] == 0:
                del letters[s[start]]
            start += 1
        m = max(m, end - start)
    return m

# examples
def main():
    print("Length of the longest substring: " 
           + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " 
           + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " 
           + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()
