class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = list()
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                low = i+1
                high = n-1
                target = -nums[i]
                while low < high:
                    if nums[low] + nums[high] == target:
                        result.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]: low += 1
                        while low < high and nums[high] == nums[high - 1]: high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1
        return result