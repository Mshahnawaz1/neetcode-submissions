class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        out = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                tmp = stk.pop()
                out[tmp] = i - tmp
            stk.append(i)
        return out