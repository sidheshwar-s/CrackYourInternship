class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = 0
        right = n - k
        cur_points = sum(cardPoints[right:])
        ans = cur_points
        
        while right < n:
            cur_points = cur_points - cardPoints[right] + cardPoints[left]
            left += 1
            right += 1
            ans = max(ans, cur_points)
        
        return ans