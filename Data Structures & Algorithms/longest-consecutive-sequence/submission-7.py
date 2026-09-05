class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        has = set(nums)
        for x in nums:
            if x-1 not in has:
                lon = 1
                while (x+lon) in has:
                    lon += 1
                res = max(res, lon)

        return res
