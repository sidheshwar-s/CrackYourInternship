class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if not(0 <= x < n and 0 <= y < m):
                return
            if grid[x][y] == "0" or grid[x][y] == "#":
                return 
            grid[x][y] = '#'
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        
        n, m = len(grid), len(grid[0])
        island_count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)
        
        return island_count