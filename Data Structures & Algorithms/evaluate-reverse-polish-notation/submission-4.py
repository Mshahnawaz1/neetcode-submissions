class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        has = {'+', '-', '*', '/'}
        for x in tokens:
            if x in has:
                l1 = int(stk.pop())
                l2 = int(stk.pop())
                if x == "+":
                    stk.append(l2 + l1)
                elif x == "-":
                    stk.append(l2 - l1)
                elif x == '/':
                    stk.append(int(l2/l1))
                else:
                    stk.append(l2*l1)

            else: stk.append(x)
        return int(stk[0])