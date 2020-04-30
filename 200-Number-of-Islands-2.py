"""
BFS Approach
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]        
        visited = set()
        cnt = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    cnt += 1
                    visited.add((i, j))
                    q.append((i, j))
                    while q != []:
                        x, y = q.pop(0)
                        for m in moves:
                            x1 = x + m[0]
                            y1 = y + m[1]
                            if len(grid) > x1 >= 0 and len(grid[0]) > y1 >= 0 and \
                                    (x1, y1) not in visited:
                                if grid[x1][y1] == '1':
                                    q.append((x1, y1))
                                visited.add((x1, y1))
                                
                visited.add((i, j))
                    

        return cnt