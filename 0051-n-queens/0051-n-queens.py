

class Solution:
    def solveNQueens(self, n):
        def is_safe(row, col):
            return not (cols[col] or diag1[row + col] or diag2[row - col + n - 1])
        
        def place_queen(row):
            if row == n:
                board = ["".join(r) for r in current_board]
                results.append(board)
                return
            
            for col in range(n):
                if is_safe(row, col):
                    cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                    current_board[row][col] = 'Q'
                    
                    place_queen(row + 1)
                    
                    current_board[row][col] = '.'
                    cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

        results = []
        current_board = [['.' for _ in range(n)] for _ in range(n)]
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)  # '\' diagonals
        diag2 = [False] * (2 * n - 1)  # '/' diagonals

        place_queen(0)
        return results

        