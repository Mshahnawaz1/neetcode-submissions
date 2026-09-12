class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        has = {}
        for i, x in enumerate(nums):
            has[x] = 1 + has.get(x, 0)
        
        for key, val in has.items():
            if val > n / 2:
                return key