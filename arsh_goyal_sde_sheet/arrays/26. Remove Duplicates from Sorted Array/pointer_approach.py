class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[pointer] = nums[i+1]
                pointer += 1
        
        return pointer