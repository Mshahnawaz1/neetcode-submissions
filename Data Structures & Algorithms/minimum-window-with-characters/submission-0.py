class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        ws, wt = {}, {}
        for x in t:
            wt[x] = 1+ wt.get(x, 0)
        
        res, L = [-1, -1], float("inf")
        have , need = 0, len(wt)

        l = 0
        for r in range(len(s)):
            c = s[r]
            ws[c] = 1 + ws.get(c, 0)
            if c in wt and wt[c] == ws[c]:
                have += 1
            while(have == need):
                if r-l+1 < L:
                    res = [l, r]
                    L = r-l+1
                ws[s[l]] -= 1
                if s[l] in wt and ws[s[l]] < wt[s[l]]:
                    have -= 1
                l = l+1
        l, r = res
        return s[l:r+1] if L != float('inf') else ""
