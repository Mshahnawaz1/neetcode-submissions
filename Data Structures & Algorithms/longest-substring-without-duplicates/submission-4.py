class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        has = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            while s[r] in has:
                has.remove(s[l])
                l += 1
            has.add(s[r])
            res = max(res, r-l+1)
            r += 1
            
        return res

