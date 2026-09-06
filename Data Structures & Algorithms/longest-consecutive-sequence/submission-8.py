class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has = set(nums)
        res = 0

        for x in has:
            if x-1 not in has:
                lon = 1
                while (x+lon in has):
                    lon += 1
                res = max(lon, res)
        return res
