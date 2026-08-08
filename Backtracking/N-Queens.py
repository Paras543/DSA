## Solve again beacuse of Syntax



class Solution(object):
    def isSafe(self, board, row, col, n):
        
        for i in range(row):
            if board[i][col] == 'Q':
                return False

      ## Left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        ## Diagnoal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nqueens(self, board, row, n, ans):
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = 'Q'

                self.nqueens(board, row + 1, n, ans)

                board[row][col] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        self.nqueens(board, 0, n, ans)

        return ans
