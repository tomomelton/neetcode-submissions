class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            if not stack:
                stack.append([i,h])
                pass
            elif h > stack[-1][1]:
                stack.append([i,h])
                pass
            
            while stack and h <= stack[-1][1]:
                i0, h0 = stack[-1]
                area = (i - i0) * h0
                if area > maxArea:
                    maxArea = area
                stack.pop()
            stack.append([i0,h])
        
        l = len(heights)
        while stack:
            i ,h = stack[-1]
            area = (l - i) * h
            if area > maxArea:
                maxArea = area
            stack.pop()

        return maxArea
