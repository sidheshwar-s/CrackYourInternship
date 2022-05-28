class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = nums[0]
        
        for n in nums:
            if count == 0:
                majority = n
                count += 1
            elif majority == n:
                count += 1
            else:
                count -= 1
        
        return majority