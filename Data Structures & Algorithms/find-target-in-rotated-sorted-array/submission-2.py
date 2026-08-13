class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot, and do normal binary search on either left or right.
        l , r = 0, len(nums) -1
        while(l<r):
            mid = l+(r-l)//2
            if nums[mid] > nums[r]:
                l  = mid + 1
            # r = mid cause we need to include the
            else: r = mid
        pivot = l

        def binaryS(l, r):
            # l, r = 0, len(nums)-1
            while(l<=r):
                mid = (l+r)//2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]: 
                    l = mid+1
                else: r = mid -1
            return -1
        
        # if target >= nums[pivot]:
        #     res = binaryS(pivot, len(nums)-1)
        # else: res = binaryS(0, pivot-1)
        res = binaryS(0, pivot-1)
        if res != -1:
            return res
        
        return binaryS(pivot, len(nums)-1)

