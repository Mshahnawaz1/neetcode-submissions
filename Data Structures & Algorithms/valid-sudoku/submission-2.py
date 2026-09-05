class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        # Rows
        for i in range(m):
            has = set()
            for j in range(n):
                cur = board[i][j]
                if cur != "." and cur in has:
                    return False
                else: has.add(cur)
        # Cols
        for i in range(n):
            has = set()
            for j in range(m):
                cur = board[j][i]
                if cur != "." and cur in has:
                    return False
                else: has.add(cur)
        #window 3*3 #assuming always 9*9 matrix
        row, col = 1,1
        for i in range(1, m, 3):
            for j in range(1, n, 3):
                has = set()
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        cur = board[i+x][j+y]
                        if cur != "." and cur in has:
                            return False
                        else: has.add(cur)
        return True
