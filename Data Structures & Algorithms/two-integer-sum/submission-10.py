class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i, x in enumerate(nums): 
            has[x] = i
        
        for i, num in enumerate(nums): 
            sub = target - num
            if sub in has and has[sub] != i:
                return [i, has[sub]]
        return []
