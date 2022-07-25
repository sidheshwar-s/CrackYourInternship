class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                x, y = queue.popleft()
                if not (0 <= x < n and 0 <= y < m):
                    continue
                if grid[x][y] == "0" or grid[x][y] == "#":
                    continue
                grid[x][y] = "#"
                queue.append((x+1, y))
                queue.append((x-1, y))
                queue.append((x, y+1))
                queue.append((x, y-1))
        
        n, m = len(grid), len(grid[0])
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    bfs(i, j)
                    
        return ans