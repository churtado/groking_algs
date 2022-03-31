"""
Given a string and a pattern, find all 
anagrams of the pattern in the given string.
"""
# implementation
def populateHash(str):
    h = {}
    for _, letter in enumerate(str):
        if letter not in h:
            h[letter] = 0
        h[letter] += 1
    return h

def find_string_anagrams(str1, pattern):
    start, end, l = 0,0,len(pattern)
    h = populateHash(pattern)
    arr = []
    while end < len(str1):
        if str1[end] in h:
            h[str1[end]] -= 1
            l -= 1
        while h[str1[end]] < 0 or (end - start + 1 > len(pattern)):
            if str1[start] in h:
                h[str1[start]] += 1
                l += 1
            start += 1
        if l == 0:
            arr.append(start)
        end += 1
    return arr

# examples
def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))

main()
