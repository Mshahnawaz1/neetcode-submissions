class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {')': '(', '}': '{', ']': '['}
        for x in s:
            if x in d:
                if stk and stk[-1] == d[x]:
                    stk.pop()
                else: return False
            else: stk.append(x)
        return True if not stk else False