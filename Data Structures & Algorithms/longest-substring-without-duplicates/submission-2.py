class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        maxLen = 0
        f = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[f])
                f += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - f + 1)
        return maxLen