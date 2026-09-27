class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        fp = 0
        rp = len(numbers) - 1

        while numbers[fp] + numbers[rp] != target:
            if numbers[fp] + numbers[rp] > target:
                rp -= 1

            elif numbers[fp] + numbers[rp] < target:
                fp += 1
                
        return [fp + 1, rp + 1]