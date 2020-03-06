
def search_word(mat, words):
    nrows, ncols = len(mat), len(mat[0])
    trie = {}
    for word in words:
        cur = trie
        for l in word:
            if not cur.get(l):
                cur[l] = {}
            cur = cur[l]
        if cur.get('$'):
            _, count = cur['$']
            cur['$'] = word, count + 1
        else:
            cur["$"] = (word, 1)
    results = []
    print(trie)
    steps = ((0, 1),(0, -1),(1, 0),(-1, 0))
    
    def dfs(i, j, cur, history):
        if cur.get('$', False):
            word, count = cur['$']
            if count > 0:
                results.append(word)
                cur['$'] = word, count - 1
            
        for ii, jj in steps:
            
            ii += i
            jj += j
            if (0 <= ii < nrows and 
                0 <= jj < ncols and 
                (ii,jj) not in history and
                cur.get(mat[ii][jj], False)
               ):
                dfs(ii, jj, cur[mat[ii][jj]], history | {(ii, jj)})
                 
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            dfs(i, j, trie, set())
    
    return results
                
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","aan","aat","rain","eat","eat"]
#     
# print(search_word(board, words))

atlas = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
        ] # 4 islands

from typing import List


def find_islands(mat: List[List[int]], word_list) -> int:
    results = []
    if not mat:
        return 0
    for word in word_list:
        visited = set()
        set_word = set(word)
        found = False
        for r, row in enumerate(mat):
            if found:
                break
            print(r, word)
            for c in range(len(row)):
                if found:
                    break
                if (r, c) not in visited and  mat[r][c] in set_word:
                    set_word.discard(mat[r][c])
                    visited.add((r, c))
                    if dfs(mat, r, c, set_word, visited, 1):
                        results.append(word)
                        found = True
            
                            
    return results

def dfs(mat,i, j, word, seen, count):
    if not word:
        return  True
    

    for r, c in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        r += i
        c += j
        if 0 <= r < len(mat) and 0 <= c < len(mat[0]) and \
        (r, c) not in seen and  mat[r][c] in word:
            word.discard(mat[r][c])
            if dfs(mat, r, c, word, seen | {(r, c)}, count + 1):
                return True
    return False

        

print(find_islands(atlas, ['oat', 'hot', 'oeiiflv']))
