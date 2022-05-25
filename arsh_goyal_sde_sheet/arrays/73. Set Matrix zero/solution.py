class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        is_first_row = any(matrix[0][c] == 0 for c in range(m))
        is_first_col = any(matrix[r][0] == 0 for r in range(n))
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] * matrix[i][0] == 0:
                    matrix[i][j] = 0 
        
        if is_first_row:
            for c in range(m):
                matrix[0][c] = 0
        
        if is_first_col:
            for r in range(n):
                matrix[r][0] = 0