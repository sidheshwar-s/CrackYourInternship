class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # eq = (yi - xi) + (yj + xj)
        queue = deque([])
        ans = -inf
        for x, y in points:
            while queue and x - queue[0][1] > k:
                queue.popleft()
            if queue: ans = max(ans, queue[0][0] + (y + x))
            while queue and queue[-1][0] <= (y-x):
                queue.pop()
            queue.append((y-x, x))
        
        return ans
            
