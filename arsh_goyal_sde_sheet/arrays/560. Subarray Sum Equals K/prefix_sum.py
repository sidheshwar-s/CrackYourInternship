class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = defaultdict(int)
        lookup[0] = 1
        n = len(nums)
        rolling_sum = 0
        count = 0
        for i in range(n):
            rolling_sum += nums[i]
            target = rolling_sum - k
            count += lookup[target]
            lookup[rolling_sum] += 1
        
        return count