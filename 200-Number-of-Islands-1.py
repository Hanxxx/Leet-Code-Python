"""
Union Find Approach
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        roots = []
        def _find_root(x, y):
            root = roots[x][y]
            while root != roots[root[0]][root[1]]:
                root = roots[root[0]][root[1]]
            i = roots[x][y]
            while i != roots[i[0]][i[1]]:
                tmp = roots[i[0]][i[1]]
                roots[i[0]][i[1]] = root
                i = tmp
            return root
        
        
        def _union(p, q):
            root_p = _find_root(p[0], p[1])
            root_q = _find_root(q[0], q[1])
            roots[root_p[0]][root_p[1]] = root_q
            
        
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    tmp.append((i, j))
                else:
                    tmp.append((-1, -1))
            roots.append(tmp)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if j - 1 >= 0 and grid[i][j - 1] == '1':
                        _union((i, j), (i, j - 1))
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        _union((i, j), (i - 1, j))
                        
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands.add(_find_root(i, j))
            
        return len(islands)