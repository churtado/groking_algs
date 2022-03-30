"""
Given a string and a pattern, find the smallest substring in the 
given string which has all the character occurrences of the given pattern.
"""
# implementation
def populateHash(str):
    h = {}
    for _, letter in enumerate(str):
        if letter not in h:
            h[letter] = 0
        h[letter] += 1
    return h

def find_substring(str1, pattern):
    start, end, l = 0,0,len(pattern)
    h = populateHash(pattern)
    m = len(str1) + 1
    mstart, mend = 0, len(str1)

    while end < len(str1):
        if str1[end] in h:
            if h[str1[end]] > 0:
                l -= 1
            h[str1[end]] -= 1
        while l == 0:
            m = min(m, end - start + 1)
            mstart, mend = start, end
            if str1[start] in h:
                if h[str1[start]] == 0:
                    l += 1
                h[str1[start]] += 1
            start += 1
        end += 1
    if m > len(str1):
        return ""
    else:
        return str1[mstart:mend+1]

# examples
def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("aabdec", "abac"))
  print(find_substring("abdbca", "abc"))
  print(find_substring("adcad", "abc")) 

main()
