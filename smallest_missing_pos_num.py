__author__ = Aneesh panoli


'''
find the smallest missing interger from an unsorted array


CONSTRAINTS:
 - smallest postive integer MISSING
 - unsorted array
 
EXAMPLE
 - a = [-1, 2, 0, 3, 4] - > 1
  -a = [1, 2, 3, 4] -> 5
  -  = [1, 2, 5, 6]
  a = [-1]
  
CLARIFYING QUESTIONS
 - are there duplicate numbers?
 - are are more than one missing  number?
 - how large the numbers can be?
 - how large can be the array?
  
INSIGHTS:
 - ignore less then zero
 - use a pointer to save the index of last seen

PoA:
EDGE cases: 
 [-1, 2, 3, 4, 5]
 
    loop through from 1 and up
 

a) sort array -> O(nlongn) + n



 '''
from typing import List

def smallest_missing_positive_number1(a: List[int]) -> int:
    
    a = sorted(a)
    if a[-1] <= 0:
        return -1
    
    for i in range(1, a[-1]):
        if i not in a:
            return i

def smallest_missing_positive_number(a: List[int]) -> int:
    if not a:
        return -1
    smallest = 1
    while True:
        if smallest not in a:
            return smallest
        smallest += 1
        
        
print(smallest_missing_positive_number([1, 2, 3]))
