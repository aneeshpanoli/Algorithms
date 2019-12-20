

def kmp_table(p):
    '''
        KMP algorithm for pattern matching
    1. Make look up table
      - compare each letters in the pattern 
      - create array of length len(p) fill with 0s
      RULES:
          1st char - i
          2nd char - j
          if two characters match
            -lookup is value in the table add 1 to it - save it as table[j]
          if no match:
            look up table[i-1]
            move i to that value
            -repeat until a match is found or i is at 0
            if match is found before reaching 0, set tbale[j] as table[i]
            if i hits 0 before a match set table[j] as 0
    '''
    table = [0]*len(p)
    i = 0
    for j in range(1, len(p)):
        if p[i] == p[j]:
            table[j] = table[i]+1
            i += 1
        else:
            while p[i] != p[j] and i != 0:
                i = table[i-1]
            table[j] = table[i]
    return table


def kmp(s, p):
    '''
     2. Perform matching
      - loop through the s as j
      - inititate i as 0 -- this is pattern index
      RULES;
        string index - i
        pattern index - j
        if match is found:
          - if j is at the end of pattern
          - append to the found index (i -j
          - set j's new value table[j]
       if no match:
          set j : table[j-1]
          --continue this until a match is found
          -- no match when j hits 0 - set j to 0
      '''
    kmp_t = kmp_table(p)
    j=0
    indices = []
    for i in range(len(s)):
        if p[j] == s[i]:
            if j == len(p)-1: #j at last index
                indices.append(i -j) # dont increment j, it will track back when a mis match arises
                j = kmp_t[j]
            else:
                j +=1
        else:
            if j > 0:
                j = kmp_t[j-1]
            else:
                j = 0
    return indices


if __name__ == '__main__':
    s = "thi sis text text"
    p = "text"
    print(kmp(s, p))
