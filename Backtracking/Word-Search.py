from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ! CurrentIdx can double as recursive depth during debugging
        self.state = False 
        self.solutionSet = []
        def backTracking(currentIdx, rowIdx, colIdx, direction): 
            print("==============")
            print(f"Current solutionSet: {self.solutionSet}")
            """
            Base cases 
            """
            if (self.state):
                print(f"self.state = true, skipping everything!!!!!")
                return
            # Error ones first -> Out of bounds --> Return to the previous recursive depth
            if (rowIdx < 0 or colIdx < 0): 
                print(f"Out of bounds with rowIdx: {rowIdx} and colIdx: {colIdx}, and currentIdx: {currentIdx}. Board was {board[rowIdx][colIdx]}, but the word was {word[currentIdx]}")
                return 

            """
            Validation logic 
            """
            # Add the current letter to the solutionSet
            if (board[rowIdx][colIdx] == word[currentIdx]):
                print(f"({rowIdx},{colIdx}) added to solutionSet")
                self.solutionSet.append((rowIdx, colIdx))

            # If the letter on the board does not match the letter in the current sequence in word[] -> return
            if (board[rowIdx][colIdx] != word[currentIdx]):
                print(f"Board letter: {board[rowIdx][colIdx]} does not match word letter: {word[currentIdx]}")
                return


            # Success case -> When currentIdx has reached the length of word - 1 
            if (currentIdx == len(word) - 1): 
                self.state = True
                print(f"CurrentIdx: {currentIdx} has reached the length of word: {word}")
                return
            
            print("Base and validation logic passed")

            """
            Directions to recurse into -> Top, Left, Bottom, Right  
            """
            # ! 1) Top --> Cannot recurse to bottom for cases where we did recurse from the bottom -> Infinite loop 
            if (direction != "Bottom"): 
                # Go up by 1 unit 
                new_row, new_col = rowIdx - 1, colIdx
                print(f"If going up --> new_row: {new_row}, new_col: {new_col}")
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and ((new_row, new_col) not in self.solutionSet):
                    print(f"Going up by 1 unit with rowIdx: {new_row} and colIdx: {new_col}; currentIdx: {currentIdx}")
                    print(f"Current word processed on the board: {board[rowIdx][colIdx]}, about to process: {board[new_row][new_col]}")
                    print("==============")
                    backTracking(currentIdx + 1, new_row, new_col, "Top")
            # 2) Right 
            if (direction != "Left"):
                new_row, new_col = rowIdx, colIdx + 1
                print(f"If going right --> new_row: {new_row}, new_col: {new_col}")
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and ((new_row, new_col) not in self.solutionSet):
                    print(f"Going right by 1 unit with rowIdx: {new_row} and colIdx: {new_col}; currentIdx: {currentIdx}")
                    print(f"Current word processed on the board: {board[rowIdx][colIdx]}, about to process: {board[new_row][new_col]}")
                    print("==============")
                    backTracking(currentIdx + 1, new_row, new_col, "Right")
            # 3) Bottom 
            if (direction != "Top"):
                new_row, new_col = rowIdx + 1, colIdx
                print(f"If going down --> new_row: {new_row}, new_col: {new_col}")
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and ((new_row, new_col) not in self.solutionSet):
                    print(f"Going down by 1 unit with rowIdx: {new_row} and colIdx: {new_col}; currentIdx: {currentIdx}")
                    print(f"Current word processed on the board: {board[rowIdx][colIdx]}, about to process: {board[new_row][new_col]}")
                    print("==============")
                    backTracking(currentIdx + 1, new_row, new_col, "Bottom")
            # 4) Left 
            if (direction != "Right"): 
                new_row, new_col = rowIdx, colIdx - 1
                print(f"If going left --> new_row: {new_row}, new_col: {new_col}")
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and ((new_row, new_col) not in self.solutionSet):
                    print(f"Going left by 1 unit with rowIdx: {new_row} and colIdx: {new_col}; currentIdx: {currentIdx}")
                    print(f"Current word processed on the board: {board[rowIdx][colIdx]}, about to process: {board[new_row][new_col]}")
                    print("==============")
                    backTracking(currentIdx + 1, new_row, new_col, "Left")
            # If all four directions don't work then that means this path doesn't work and we pop
            self.solutionSet.pop()
        
        """
        For-loop through the board until we find the start letter that works; if not then we keep looping
        -If found then start backTracking
        """
        
        for row in range(0, len(board)): 
            for col in range(0, len(board[0])):
                if (board[row][col] == word[0]):
                    # * Don't add direction in the first pass
                    print(f"Starting backTracking with rowIdx: {row} and colIdx: {col}")
                    backTracking(0, row, col, "")
                    if (self.state): 
                        return True   
                    # If we are back here and no solutipn, then that means we need to clear the state 
                    self.solutionSet = set()

        
        return self.state   