class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        bool is_first_row = false, is_first_col = false;
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(matrix[i][j] == 0) {
                    if(i == 0) is_first_row = true;
                    if(j == 0) is_first_col = true;
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        
        for(int i = 1; i < n; i++) {
            for(int j = 1; j < m; j++) {
                if(matrix[0][j] == 0 || matrix[i][0] == 0) {
                    matrix[i][j] = 0;
                }
            } 
        }
        
        if(is_first_row) {
            for(int j = 0; j < m; j++) matrix[0][j] = 0;
        }
        
        if(is_first_col) {
            for(int i = 0; i < n; i++) matrix[i][0] = 0;
        }
    }
};