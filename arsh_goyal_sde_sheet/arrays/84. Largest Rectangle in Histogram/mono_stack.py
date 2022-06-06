class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initialise out monotonic stack and final answer
        stack, ans = [], 0
        
        # loop for index, height 
        for i, h in enumerate(heights + [0]):
            
            # if current height violates the monotonicity, remove untill its strictly increasing
            while stack and heights[stack[-1]] >= h:
                
                H = heights[stack.pop()]
                
                # if there isn't a stack its obvious that current height is the smallest so far
                W = i if not stack else i-stack[-1]-1
                
                # calculate and store the maximum area 
                ans = max(ans, H*W)
            
            # finally we store the index in stack
            stack.append(i)
        
        return ans