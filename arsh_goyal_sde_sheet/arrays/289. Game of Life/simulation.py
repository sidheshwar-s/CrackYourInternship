class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        10 - 2
        00 - 0
        11 - 3
        01 - 1
        """
        m, n = len(board), len(board[0])
        
        def get_count(i, j):
            neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
            living = dead = 0
            for x, y in neighbours:
                dx = i + x
                dy = j + y
                if (0 <= dx < m and 0 <= dy < n):
                    if board[dx][dy] == 0 or board[dx][dy] == 2:
                        dead += 1
                    else:
                        living += 1
            
            return living, dead
            
        for i in range(m):
            for j in range(n):
                living, dead = get_count(i, j)
                if (living < 2 or living > 3) and (board[i][j] == 1 or board[i][j] == 3):
                    board[i][j] = 1
                elif (board[i][j] == 0 or board[i][j] == 2) and living == 3:
                    board[i][j] = 2
                elif (living == 2 or living == 3) and (board[i][j] == 1 or board[i][j] == 3):
                    board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
                
                    
        
                    