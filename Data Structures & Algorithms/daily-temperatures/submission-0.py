class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0]*n
        stack = []
        for i in range(n):
            while(stack and temperatures[stack[-1]] < temperatures[i]):
                prev = stack.pop()
                results[prev] = i - prev
            stack.append(i)
        return results