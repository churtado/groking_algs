"""
Given a string and a list of words, 
find all the starting indices of 
substrings in the given string that 
are a concatenation of all the given 
words exactly once without any 
overlapping of words. 
It is given that all words are of the same length.
"""
# implementation
def getHash(words):
    h = {}
    for word in words:
        if word not in h:
            h[word] = 0
        h[word] += 1
    return h

def find_word_concatenation(str1, words):
    h = getHash(words)
    start, end = 0,0
    wl = len(words[0])
    l = len(words)
    r = []
    while end < len(str1):
        if str1[end:end+wl] in h:
            if h[str1[end:end+wl]] > 0:
                l -= 1
            h[str1[end:end+wl]] -= 1
        while h[str1[end:end+wl]] < 0:
            h[str1[start:start+wl]] += 1
            if h[str1[start:start+wl]] > 0:
                l += 1
            start += wl
        if l == 0:
            r.append(start)
        end += wl
    return r


# examples
def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))

main()
