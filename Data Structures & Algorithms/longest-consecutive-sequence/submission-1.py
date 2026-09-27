class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = [0]
        for num in set(nums):
            if num - 1 not in nums:
                length = 0
                while num in nums:
                    length += 1
                    num += 1
                lengths.append(length)
        return max(lengths)