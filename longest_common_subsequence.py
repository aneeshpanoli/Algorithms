__author__ = Aneesh Panoli

def find_common_subsequence(s: str, ss: str) -> str:
    if not s or not ss:
        return ""
    lcss = ""
    s_range_limit = 0
    for i in range(len(ss)): 
        for j in range(s_range_limit, len(s)): # o(n*m)
            if ss[i] == s[j]:
                lcss += ss[i]
                s_range_limit = i + 1
                break
    return lcss



print(find_common_subsequence('aa', 'aa')) # aa
print(find_common_subsequence('axxxa', 'aa')) # aa
print(find_common_subsequence('xxxaxxxa', 'aa')) # aa
print(find_common_subsequence('aa', 'axxxaa')) # aa
print(find_common_subsequence('', 'aa')) # ""
print(find_common_subsequence('a', '')) # ""


#brute force # 2
def find_the_lowest_common_sub_sequence(s: str, p: str) -> str:
    if not p or not s:
        return ""
    common_ss = ""
    i_limit = len(s)
    p = list(p) # time O(n), space = O(n)
    for _ in range(len(p)):
        char = p.pop()
        for i in range(i_limit - 1, -1, -1): 
            if s[i] == char:
                common_ss = char + common_ss
                i_limit -=  i 
                break
    return common_ss
        
        

print(find_the_lowest_common_sub_sequence("abxbxxbx", "xab"))
