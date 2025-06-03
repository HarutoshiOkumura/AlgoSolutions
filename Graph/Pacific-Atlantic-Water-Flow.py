# from typing import List
from collections import deque # Corrected import
"""
Brute-Force Multi-Source BFS every single cell? 

Thoughts: 
    1) From what I have seen, even if immediate left and up are blocked (directions to Pacific Ocean), you can still flow around it by taking bottom and right (directions to Atlantic Ocean)
"""

"""
Implementation Plan: 
    1) Iterate the outer perimiter (rowIdx && colIdx < 0 for Pacific Ocean)
    2) Iterate the outer perimiter (rowIdx && colidx >= len(grid), len(grid[rowIdx]) for Atlantic Ocean)
    3) Logic for perimiter iteration: 
        a) For each square on the border, check if there are any squares that are higher than or equal to the current grid 
        b) Use a set() to keep track of square coordinates (rowIdx,colIdx) that already exists; one set for each Ocean type 
    4) For all the square coordinates that are in both Atlantic and Pacific, are returned 
    5) First pass Pacific, second pass Atlantic, and on second pass we also find the squares that do have overlap   
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        pacificOcean = set()
        atlanticOcean = set() # Added set for Atlantic Ocean
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # Top, Right, Bottom, Left
        # visitedSquares = set() # This will be handled by ocean-specific sets
        # answerSet = [] # Will be populated at the end

        ROWS, COLS = len(heights), len(heights[0])

        # * ================================
        # * Function to simulate reverse waterflow
        # * ================================
        def waterFlow(initialRowIdx, initialColIdx, target_ocean_set):
            # If the starting cell for this BFS is already in the target_ocean_set,
            # it means it has been visited by a previous BFS for the SAME ocean. So, skip.
            if (initialRowIdx, initialColIdx) in target_ocean_set:
                return

            queue = deque()
            queue.append((initialRowIdx, initialColIdx))
            target_ocean_set.add((initialRowIdx, initialColIdx)) # Add starting cell to its ocean set

            while len(queue) > 0:
                rowIdx, colIdx = queue.popleft()
                currentSquareHeight = heights[rowIdx][colIdx]

                for x, y in directions:
                    newRowIdx, newColIdx = rowIdx + x, colIdx + y

                    # Out of bounds check
                    if not (0 <= newRowIdx < ROWS and 0 <= newColIdx < COLS):
                        continue

                    # If already processed for this ocean, skip
                    if (newRowIdx, newColIdx) in target_ocean_set:
                        continue

                    neighborSquareHeight = heights[newRowIdx][newColIdx]

                    # ! CRITICAL FIX: Water flows from neighbor to current cell if neighbor_height >= current_height
                    if neighborSquareHeight >= currentSquareHeight:
                        target_ocean_set.add((newRowIdx, newColIdx))
                        queue.append((newRowIdx,newColIdx))
        # * =======================================================================================================

        # TODO: Pacific Ocean Border Iteration
        # * A) Everything on the top row
        for colIdx in range(COLS):
            waterFlow(0, colIdx, pacificOcean)

        # * B) Everything on the leftest column (remaining cells)
        for rowIdx in range(1, ROWS): # Starts from 1 as (0,0) is covered by top row
            waterFlow(rowIdx, 0, pacificOcean)

        # TODO: Atlantic Ocean Border Iteration
        # * C) Everything on the bottom row
        for colIdx in range(COLS):
            waterFlow(ROWS - 1, colIdx, atlanticOcean)

        # * D) Everything on the rightest column (remaining cells)
        for rowIdx in range(ROWS - 1): # Iterate up to ROWS-2, as (ROWS-1, COLS-1) is covered by bottom row
            waterFlow(rowIdx, COLS - 1, atlanticOcean)

        # * =======================================================================================================
        # * Find cells reachable by both oceans
        # * =======================================================================================================
        answerSet = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacificOcean and (r, c) in atlanticOcean:
                    answerSet.append([r, c])
        
        return answerSet



