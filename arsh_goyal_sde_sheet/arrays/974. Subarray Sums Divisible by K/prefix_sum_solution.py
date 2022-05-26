class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        lookup = defaultdict(int)
        rolling_sum = 0
        result = 0
        lookup[0] = 1
        for n in nums:
            rolling_sum += n
            rem = rolling_sum % k
            result += lookup[rem]
            lookup[rem] += 1
        return result