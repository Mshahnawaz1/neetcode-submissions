class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in match.values():          # opening bracket
                stack.append(ch)
            else:                             # closing bracket
                if not stack or stack[-1] != match.get(ch):
                    return False
                stack.pop()

        return not stack