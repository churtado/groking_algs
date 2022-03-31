"""
Given a string and a pattern, find out if the string 
contains any permutation of the pattern.
"""
# implementation
def find_permutation(str1, pattern):
    start, end = 0,0
    l = len(pattern)
    h = {}
    for _, letter in enumerate(pattern):
        if letter not in h:
            h[letter] = 0
        h[letter] += 1

    while end < len(str1):
        if str1[end] in h and h[str1[end]] > 0:
            h[str1[end]] -= 1
            l -= 1
        else:
            while start < end:
                if str1[start] in h:
                    h[str1[start]] += 1
                    l += 1
                start += 1
        if l == 0:
            return True
        end += 1
    return False

# examples
def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

main()
