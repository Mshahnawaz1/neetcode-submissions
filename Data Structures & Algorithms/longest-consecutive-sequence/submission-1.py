class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # li = {x: 1 for x in set(nums)}
        lon = 0 
        # has = {x:0 for x in set(nums)}
        has = set(nums)
        
        for x in nums:
            cur = x
            count = 1
            
            if x - 1 not in has:
                while((cur + 1) in has):
                    cur += 1
                    count += 1
                lon = max(lon, count)
        return lon

