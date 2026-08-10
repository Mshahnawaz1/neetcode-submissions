class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sk, tk = {}, {}
        for i in range(len(s)):
            sk[s[i]] = 1+ sk.get(s[i], 0)
            tk[t[i]] = 1+ tk.get(t[i],0)
        return sk == tk