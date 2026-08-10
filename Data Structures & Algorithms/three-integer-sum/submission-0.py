class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range (len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) -1 
            while l < r:
                sum = nums[l]+nums[r]+nums[i]
                if sum == 0:
                    out.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while(nums[l] == nums[l-1] and l < r): l+=1
                elif sum > 0:
                    r -= 1
                else:
                    l +=1

        return out

                    