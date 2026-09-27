class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        freq[0] = 0
        for n in nums:
            freq[n] += 1
        if max(freq.values()) > 1:
            return True 
        return False
         