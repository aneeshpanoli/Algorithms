mat = [
    [1, 2, 3, 1],
    [4, 5, 6, 2],
    [7, 8, 9, 3],
    [23, 34, 45, 43]
      ]


def print_diag(mat):
    visited = set([(0, 0)])
    i, j = 0, 0
    print(mat[i][j])
    while len(visited) < len(mat) * len(mat[0]):
        for r, c in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            # keep going until the index reach the end of the current row
            while (i+ r, j+c) not in visited and 0 <=  i+r < len(mat) and 0 <= j+c < len(mat[0]):
                i += r
                j += c
                visited.add((i, j))
                print(mat[i][j])

                    
        
print_diag(mat) 
