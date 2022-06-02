class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # eq = (yi - xi) + (yj + xj)
        heap = []
        ans = -inf
        for x, y in points:
            while heap and x - heap[0][1] > k:
                heappop(heap)
            if heap: ans = max(ans, -heap[0][0] + (y + x))
            heappush(heap, (-(y - x), x))
        
        return ans
            
        