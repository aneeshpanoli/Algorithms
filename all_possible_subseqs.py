'''
given strA and strB find subsequences

strA -> 'AB'
strB -> 'ABAB'
subsequences : AB, A__B, AB 
output -> 3

1. for every c in strA:
    see if it is in strB
     as soon as we find the first letter
      we look for the next letter and so on
      
     0 a b a b    
  0  1 1 1 1 1
  a  0 1 1 2 2
  b  0 0 1 1 3

'''

def num_sub_sequences(str_a, str_b):
    mat = [[0 for i in range(len(str_b)+1)] for j in range(len(str_a)+1)]
    
    for i, c_a in enumerate(str_a):            
        for j, c_b in enumerate(str_b):
            if i == 0:
                mat[i][j] = 1
            if c_a == c_b:
                mat[i+1][j+1] = mat[i+1][j] + mat[i][j]
            else:
                mat[i+1][j+1] = mat[i+1][j]
    print(mat)
            
    return mat[i+1][j+1]
                

    
        
    
    
print(num_sub_sequences('ab', 'abab'))
