
__author__ = "Aneesh Panoli"

from typing import List
def grep(s: str, p:str) -> List[int]:
    seen = []
    needle_hash = hash(p)
    
    for i in range(len(s) - len(p) +1):
        if hash(s[i: i+len(p)] ) == needle_hash:
            seen.append(i)
    return seen

def hash(s: str) -> int:
    index = 0
    for i, char in enumerate(s):
        index += ord(char) * 256 ** i
    return index


print(grep('abaaabababba','aba')
