class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l-1):
            for j in range(1, l) :
                if i == j:
                    continue
                if nums[i] +nums [j] == target:
                    return [i,j]