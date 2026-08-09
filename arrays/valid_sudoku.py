class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.validate_rows(board)
            and self.validate_columns(board)
            and self.validate_squares(board)
        )

    def validate_rows(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.validate_unit(row):
                continue
            return False
        return True

    def validate_columns(self, board: List[List[str]]) -> bool:
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if self.validate_unit(column):
                continue
            return False
        return True

    def validate_squares(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if self.validate_square(board, i, j):
                    continue
                return False
        return True

    def validate_square(self, board: List[List[str]], x: int, y: int) -> bool:
        square = []
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                square.append(board[i][j])
        return self.validate_unit(square)

    def validate_unit(self, unit: List[str]) -> bool:
        digits = set()
        for i in unit:
            if i == ".":
                continue
            if i in digits:
                return False
            digits.add(i)
        return True