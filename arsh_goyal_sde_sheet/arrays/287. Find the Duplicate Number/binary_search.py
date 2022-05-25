class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            count = sum(n <= mid for n in nums)
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        
        return low