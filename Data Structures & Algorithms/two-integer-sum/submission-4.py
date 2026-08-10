class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indi = {}
        for i, n in enumerate(nums):
            indi[n] = i

        for i, n in enumerate(nums):
            dif = target - n
            if dif in indi and indi[dif] != i:
                return [i,indi[dif]]