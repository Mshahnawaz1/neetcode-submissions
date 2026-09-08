class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i, x in enumerate(nums):
            # all positives
            # if x > 0: break
            if i > 0 and x == nums[i-1]: continue #skip the duplicate start

            L, R = i+1, len(nums)-1
            while L < R:
                cur = x+nums[L] + nums[R]
                if cur > 0: R -= 1
                elif cur < 0: L += 1
                else:
                    out.append([x, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L-1] == nums[L] and L < R:
                        L += 1
        return out
