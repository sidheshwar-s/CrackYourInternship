class Solution:
    def findPath(self, m, n):
        # code here
        def dfs(x, y, path):
            if not (0 <= x < n and 0 <= y < n):
                return 
            if m[x][y] == 0:
                return
            if x == n-1 and y == n-1:
                ans.add(path)
                return
            m[x][y] = 0
            dfs(x-1, y, path + 'U')
            dfs(x+1, y, path + 'D')
            dfs(x, y-1, path + 'L')
            dfs(x, y+1, path + 'R')
            m[x][y] = 1
        ans = set()
        dfs(0, 0, "")
        return list(ans)