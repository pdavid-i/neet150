class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = {}
        pdiag = {}
        ndiag = {}
        board = [["." for j in range(n)] for i in range(n)]
        sol = []

        def backtrack(row):
            if row > n:
                return
            if row == n:
                sol.append(["".join(row) for row in board].copy())
                return
            for col in range(n):
                if col in cols or row - col in ndiag or row + col in pdiag:
                    continue
                board[col][row] = 'Q'
                cols[col] = True
                pdiag[row + col] = True
                ndiag[row - col] = True
                backtrack(row+1)
                board[col][row] = '.'
                cols.pop(col)
                pdiag.pop(row+col)
                ndiag.pop(row-col)
        backtrack(0)
        return sol
