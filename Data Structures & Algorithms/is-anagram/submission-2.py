class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = defaultdict(int)
        freqT = defaultdict(int)

        if len(s) == len(t):
            for c in s:
                freqS[c] += 1
            for c in t:
                freqT[c] += 1
            if freqS.items() == freqT.items():
                return True
        return False