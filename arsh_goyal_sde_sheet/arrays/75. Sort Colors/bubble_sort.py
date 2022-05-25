class Solution:
    # bubble sort
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        for i in range(N):
            already_sorted = True
            for j in range(N-i-1):
                if nums[j] > nums[j+1]:
                    already_sorted = False
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            
            # slight optimisation
            if already_sorted: break
        
        