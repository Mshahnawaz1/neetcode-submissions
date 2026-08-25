class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set(nums)
        return False if len(l) == len(nums) else True