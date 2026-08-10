class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        # for i in range(0, len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if i != j:
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]
        
        has = {num: i for i, num in enumerate(nums)}
        for j, x in enumerate(nums):
            ch = target-x
            if ch in has and not j == has[ch] :
                return [j, has[ch]]