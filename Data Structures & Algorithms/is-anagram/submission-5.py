class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # li = list(s)
        # for x in t:
        #     if x in li:
        #         li.pop(x)
        # return True if len(li) == 0 else False
