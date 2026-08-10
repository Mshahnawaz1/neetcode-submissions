class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if nums == list(set(nums)):
        #     return False
        # return True
        if len(set(nums)) == len(nums):
            return False
        return True
            