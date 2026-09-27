class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for x, n in enumerate(nums):
            if n > 0:
                break

            if x > 0 and n == nums[x - 1]:
                continue

            f = x + 1
            r = len(nums) - 1

            while f < r:
                sum = n + nums[f] + nums[r]
                if sum < 0:
                    f += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([n, nums[f], nums[r]])
                    f += 1
                    r -= 1
                    while nums[f] == nums[f - 1] and f < r:
                        f += 1

        return res