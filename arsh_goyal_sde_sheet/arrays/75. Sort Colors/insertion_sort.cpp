class Solution {
public:
    void sortColors(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++) {
            int cur = nums[i];
            int j = i - 1;
            while (j >= 0 && nums[j] > cur) {
                nums[j + 1] = nums[j];
                j -= 1;
            }
            nums[j+1] = cur;
        }
    }
};