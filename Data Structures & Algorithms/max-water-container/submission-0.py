class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        f, r = 0, len(heights) - 1

        while f < r:
            if heights[f] < heights[r]:
                a = heights[f] * (r - f)
                f += 1
            else:
                a = heights[r] * (r - f)
                r -= 1
            
            if a > maxArea:
                maxArea = a

        return maxArea
