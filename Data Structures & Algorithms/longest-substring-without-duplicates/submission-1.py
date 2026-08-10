class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[R])
            longest = max(R-left+1, longest)
        return longest