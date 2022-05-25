class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red = 0, white = 0, blue = nums.size() - 1;
        
        while(white <= blue) {
            if(nums[white] == 0) {
                swap(nums[white++], nums[red]);
                red ++;
                white ++;
            } else if(nums[white] == 1) {
                white ++;
            } else {
                swap(nums[white], nums[blue]);
                blue --;
            }
        }
    }
};