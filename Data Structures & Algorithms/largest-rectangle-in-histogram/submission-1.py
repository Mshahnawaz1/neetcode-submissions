class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0
        leftMost, rightMost = [-1]*n, [n]*n

        for i in range(n):
            while(stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = [] 
        for i in range(n-1, -1, -1):
            while(stack and heights[stack[-1]] >= heights[i]):
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1

            curr = (rightMost[i] - leftMost[i]+1) * heights[i]
            maxArea = max(curr, maxArea)
        return maxArea
