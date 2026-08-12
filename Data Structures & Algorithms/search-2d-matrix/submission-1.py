class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        while (top <= bottom):
            midR = top + (bottom-top) // 2

            left, right = 0, cols - 1
            while(left <= right):
                midC = left + (right-left) //2
                curr = matrix[midR][midC]
                if target == curr:
                    return True
                elif target > curr: left = midC + 1
                else : right = midC - 1

            currRL = matrix[midR][0]
            currRR = matrix[midR][cols-1]
            if target > currRR:
                top = midR+1
            else: bottom = midR - 1

        return False