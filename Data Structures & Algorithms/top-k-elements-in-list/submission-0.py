class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = defaultdict(list)
        for n in nums:
            numFreq[n].append(n)
        numFreq = dict(numFreq)
        return sorted(numFreq, key=lambda key: len(numFreq[key]))[-k:]