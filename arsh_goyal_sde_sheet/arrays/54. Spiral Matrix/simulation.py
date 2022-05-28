class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        min_r = min_c = 0
        max_r, max_c = n, m
        result = []
        
        while min_r < max_r and min_c < max_c:
            # top 
            if min_r < max_r:
                for i in range(min_c, max_c):
                    result.append(matrix[min_r][i])
                min_r += 1
        
            # right
            if min_c < max_c:
                for i in range(min_r, max_r):
                    result.append(matrix[i][max_c-1])
                max_c -= 1
            
            # bottom
            if min_r < max_r:
                for i in range(max_c-1, min_c-1, -1):
                    result.append(matrix[max_r-1][i])
                max_r -= 1
            
            # left
            if min_c < max_c:
                for i in range(max_r-1, min_r-1, -1):
                    result.append(matrix[i][min_c])
                min_c += 1
        
        return result