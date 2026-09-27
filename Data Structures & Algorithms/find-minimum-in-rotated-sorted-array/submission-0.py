class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        f, r = 0, len(nums)-1

        while f < r:
            m = f + (r - f) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                f = m + 1

        return nums[f]