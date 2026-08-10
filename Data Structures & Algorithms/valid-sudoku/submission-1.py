class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                el = board[i][j]

                if el == ".":
                    continue
                bo = (i // 3) * 3  + (j // 3)
                if el in row[i] or el in col[j] or el in box[bo]:
                    return False

                row[i].add(el)
                col[j].add(el)
                box[bo].add(el)
        return True
