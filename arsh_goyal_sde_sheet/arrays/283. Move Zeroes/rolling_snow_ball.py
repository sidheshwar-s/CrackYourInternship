# inspired by post https://leetcode.com/problems/move-zeroes/discuss/172432/THE-EASIEST-but-UNUSUAL-snowball-JAVA-solution-BEATS-100-(O(n))-+-clear-explanation

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ballSize = 0
        N = len(nums)
        
        for i in range(N):
            if nums[i] == 0:
                ballSize += 1
            else:
                nums[i], nums[i-ballSize] = 0, nums[i]