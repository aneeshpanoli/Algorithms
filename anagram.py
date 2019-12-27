__author__ = Aneesh Panoli


'''
from typing import Dict
from collections import defaultdict
def find_anagram(s: str, a: str) -> bool:
    if len(s) != len(a):
        return False
            
    return count_chars(s) == count_chars(a)
    
    
def count_chars(s: str) -> Dict[str, int]:
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    return counter
    
