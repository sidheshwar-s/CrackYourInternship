class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1, n-2):
                    if j == i+1 or nums[j] != nums[j-1]:
                        left = j + 1  
                        right = n - 1
                        cur_target = target - (nums[i] + nums[j])
                        while left < right:
                            if nums[left] + nums[right] == cur_target:
                                result.append([nums[i], nums[j], nums[left], nums[right]])
                                while left < right and nums[left] == nums[left + 1]: left += 1
                                while left < right and nums[right] == nums[right - 1]: right -= 1
                                left += 1
                                right -= 1
                            elif nums[left] + nums[right] < cur_target:
                                left += 1
                            else:
                                right -= 1
        
        return result