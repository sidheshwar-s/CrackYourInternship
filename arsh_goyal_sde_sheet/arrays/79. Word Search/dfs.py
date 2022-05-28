class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def find(x, y, index):
            if index == len(word):
                return True
            if not (0 <= x < n and 0 <= y < m):
                return False
            if board[x][y] == word[index]:
                board[x][y] = " "
                up = find(x-1, y, index+1)
                down = find(x+1, y, index+1)
                left = find(x, y-1, index+1)
                right = find(x, y+1, index+1)
                board[x][y] = word[index]
                return up or down or left or right
            else:
                return False
            
        start_pos = []
        C = Counter(word)
        
        for i in range(n):
            for j in range(m):
                C[board[i][j]] -= 1
                if board[i][j] == word[0]:
                    start_pos.append((i, j))
        
        if max(C.values()) > 0: return False
        
        for r, c in start_pos:
            if find(r, c, 0): return True
        
        return False