class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int ballSize = 0, N = nums.size();
        for(int i = 0; i < N; i++) {
            if(nums[i] == 0) ballSize++;
            else {
                int temp = nums[i];
                nums[i] = 0;
                nums[i-ballSize] = temp;
            }
        }
    }
};