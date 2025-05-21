from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        For-loop through the board until we find the start letter that works; if not then we keep looping
            -If found then start backTracking
        """
        self.state = False 
        # ! CurrentIdx can double as recursive depth during debugging
        def backTracking(currentIdx, rowIdx, colIdx, direction): 
            """
            Base cases 
            """
            # Error ones first -> Out of bounds --> Return to the previous recursive depth
            if (rowIdx < 0 or colIdx < 0): 
                return 


            # Success case -> When currentIdx has reached the length of word - 1 
            if (currentIdx > len(word)): 
                self.state.true
                return
            
            """
            Validation logic 
            """
            # If the letter on the board does not match the letter in the current sequence in word[] -> return
            if (board[rowIdx][colIdx] != word[currentIdx]):
                return


            """
            Directions to recurse into -> Top, Left, Bottom, Right  
            """
            # ! 1) Top --> Cannot recurse to bottom for cases where we did recurse from the bottom -> Infinite loop 
            if (direction != "Bottom"): 
                # Go up by 1 unit 
                backTracking(currentIdx + 1, rowIdx - 1, colIdx, "Top")
            # 2) Right 
            if (direction != "Left"):
                backTracking(currentIdx + 1, rowIdx, colIdx + 1, "Right")
            # 3) Bottom 
            if (direction != "Top"):
                backTracking(currentIdx + 1, rowIdx - 1, colIdx, "Bottom")
            # 4) Left 
            if (direction != "Right"): 
                backTracking(currentIdx + 1, rowIdx, colIdx - 1, "Left")
            

        
        return self.state