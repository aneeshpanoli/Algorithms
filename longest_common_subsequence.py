#brute force
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
