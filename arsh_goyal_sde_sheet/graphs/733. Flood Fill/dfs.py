class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m):
                return 
            if image[x][y] == color:
                return 
            if image[x][y] != match: 
                return 
            image[x][y] = color
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        
        n, m = len(image), len(image[0])
        match = image[sr][sc]
        dfs(sr, sc)
        return image