class Solution {
public:
    void sortColors(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++) {
            bool is_sorted = true;
            for(int j = 0; j < nums.size() - i - 1; j ++) {
                if(nums[j] > nums[j+1]) {
                    swap(nums[j], nums[j+1]);
                    is_sorted = false;
                }
            }
            if(is_sorted) break;
        }
    }
};