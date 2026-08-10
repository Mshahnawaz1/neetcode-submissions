class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pla = {}
        # for i, x in enumerate(nums):
        #     pla[x] = nums.pop(x)
        out = []
        for i,x in enumerate(nums):
            prd = 1
            for j, y in enumerate(nums):
                if i == j:
                    continue
                prd *= y
            out.append(prd)
        return out
