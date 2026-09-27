class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        f, r = 0, len(nums) - 1

        while f <= r:
            mid = ((r - f) // 2) + f
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                f = mid + 1
            else:
                return mid
        
        return -1
