class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i, n in enumerate(nums):
            if target-n in lookup:
                idx = lookup[target-n]
                return [idx, i]
            lookup[n] = i
            