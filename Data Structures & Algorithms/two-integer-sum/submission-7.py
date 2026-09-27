class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i = 0
        j = 0

        for index in range(len(nums)-1, -1, -1):
            if not i:
                difference = target - nums[index]

                if difference in nums[:index]:
                    i = index

            elif nums[index] + nums[i] == target:
                j = index

        return [j, i]