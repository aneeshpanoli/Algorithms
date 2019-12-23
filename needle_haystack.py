#s: haystack
#p: Needle

def str_str(s, p):
    j = 0
    for i in range(len(s)):
        if s[i] != p[j]:
            # once i - len(i) is less than len(p)
            # and there is mismatch, then there will never be a match beyond that point
            if i == len(s) -len(p)+1:
                return -1
            j = 0
        else:
        #once j reaches the last element of p
        # we can exit as we have found a match
            if j == len(p) -1:
                return i - j
            j += 1
