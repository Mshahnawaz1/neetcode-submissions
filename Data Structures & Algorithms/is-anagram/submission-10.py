class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # has = {}
        # hat = {}
        # for x in s:
        #     has[x] = 1+ has.get(x, 0)
        # for x in t:
        #     hat[x] = 1+ hat.get(x, 0)
        # return has == hat
        return sorted(s) == sorted(t)
