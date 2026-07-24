class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_occurences = {}
        col_occurences = {}
        square_occurences = {}
        for i in range(9):
            row_occurences[i] = []
            col_occurences[i] = []
            square_occurences[i] = []
        
        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el == ".":
                    continue
                square_idx = (i // 3) * 3 + (j // 3)
                if (el in row_occurences[i]) or (el in col_occurences[j]) or (el in square_occurences[square_idx]):
                    print(el)
                    print(i, row_occurences[i])
                    print(j, col_occurences[j])
                    print(square_idx, square_occurences[square_idx])
                    return False
                row_occurences[i].append(el)
                col_occurences[j].append(el)
                square_occurences[square_idx].append(el)
        return True



