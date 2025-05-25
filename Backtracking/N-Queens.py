from typing import List

"""
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
"""

"""
Notes:
1. Loop over each row, backtrack on each square iteratively; moving on to the next column when all of its rows' square fails 
9
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize n x n board with '.' representing empty cells
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        # ! List to store all valid solutions
        self.solutions = []
        
        def isValid(rowIdx, colIdx, n):
            # ! Base case: if we've gone beyond the board, return False
            if rowIdx >= n:
                return False
                
            # ! 1) Horizontal check - if current row has a queen
            if "Q" in self.board[rowIdx]:
                return False
                
            # ! 2) Vertical check - if current column has a queen above
            for row in range(rowIdx):
                if self.board[row][colIdx] == 'Q':
                    return False
                    
            # ! 3) Diagonal checks
            # Check upper-left diagonal
            row, col = rowIdx - 1, colIdx - 1
            while row >= 0 and col >= 0:
                if self.board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
                
            # Check upper-right diagonal
            row, col = rowIdx - 1, colIdx + 1
            while row >= 0 and col < n:
                if self.board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
                
            return True
        
        def backTracking(rowIdx, Qcount):
            # ! Base case: if we've placed n queens, we found a solution
            if Qcount == n:
                # ! Solution found - convert board to required format and add to solutions
                solution = [''.join(row) for row in self.board]
                self.solutions.append(solution)
                return
                
            # * For loop, to loop through all of the row's potential 
            for colIdx in range(n):
                # TODO: It seems like Queen's validation logic should be in the base cases 
                # TODO: Accounts for diagonal, vertical and horizontal
                if not isValid(rowIdx, colIdx, n):
                    continue
                
                # Insert the candidateQueen in the current row (as the anchor)
                    # ! Only append if the check validates it? 
                self.board[rowIdx][colIdx] = "Q"
                # TODO: Then recurse into the next layer --> one row deeper
                backTracking(rowIdx + 1, Qcount + 1)

                # TODO: Then remove the current Queen's position if the recursive call fails for a different iteration 
                self.board[rowIdx][colIdx] = "."
                # ! Qcount -= 1
                """
                I removed the Qcount -= 1 line because:
                Qcount is passed as a parameter to the recursive call
                Each recursive call gets its own copy of Qcount
                When we backtrack, we don't need to decrement Qcount because:
                The original Qcount value is preserved in the current function call
                The next iteration of the loop will use the original Qcount value
                The recursive call with Qcount + 1 handles the increment
                This should fix the empty array issue because:
                Qcount will now properly track the number of queens placed
                When Qcount == n, we'll correctly identify a solution
                The backtracking will properly explore all possible configurations
                """
        

        # ? Iteratively call backTracking for the recursive layer below it --> Goes through each unit row by row
            # ! Scratch it, makes more sense to loop for each row inside of the recursive call 
        backTracking(0, 0)
        return self.solutions 