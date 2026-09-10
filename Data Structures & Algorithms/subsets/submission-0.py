class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        subsets = []
        def dfs(i):
            if i >= len(nums):
                out.append(subsets.copy())
                return
            # add the number
            subsets.append(nums[i])
            dfs(i+1)
            # dont add the number
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return out