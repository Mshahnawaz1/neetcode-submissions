class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        m, n = len(strs[0]), len(strs)

        for j in range(m):
            for i in range(1, n):
                if j == len(strs[i]) or strs[0][j] != strs[i][j]:
                    return strs[0][:j]
        return strs[0]
            
