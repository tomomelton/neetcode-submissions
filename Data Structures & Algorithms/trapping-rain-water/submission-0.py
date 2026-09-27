class Solution:
    def trap(self, height: List[int]) -> int:

        f, r = 0, len(height) - 1
        maxf, maxr = height[f], height[r]
        area = 0

        while f < r:
            s = 0
            if height[f] > height[r]:
                s = maxr - height[r]
                maxr = max(maxr, height[r])
                r -=1
            else:
                s = maxf - height[f]
                maxf = max(maxf, height[f])
                f += 1
            area += max(0, s)

        return area