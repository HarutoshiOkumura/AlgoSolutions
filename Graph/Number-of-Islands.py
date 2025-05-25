from typing import List 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ! Data Structure Choice: Using set() with tuples instead of lists
        # * Tuples are immutable (cannot be modified after creation) and hashable
        # * Lists are mutable (can be modified) and therefore not hashable
        # * Sets in Python require hashable elements because they use hash tables internally
        # * Using tuples for coordinates is ideal because:
        #   - Coordinates don't need to be modified once created
        #   - Tuples are more memory efficient than lists
        #   - Tuples can be used as dictionary keys or set elements
        #   - Tuples maintain the order of coordinates (row, col)
        self.registeredIslands = set() 
        self.rowLength = len(grid)
        if self.rowLength == 0: # Handle empty grid
            return 0
        self.colLength = len(grid[0])
        if self.colLength == 0: # Handle grid with empty rows
            return 0
        self.islandCount = 0
        

        def dfs(rowIdx,colIdx): 
            """
            Base Case Handeling 
            """
            # Out of bounds base-case 
            if not (0 <= rowIdx < self.rowLength and 0 <= colIdx < self.colLength): 
                return
            # Check if water or already visited (must be after bounds check)
            if grid[rowIdx][colIdx] == '0' or (rowIdx, colIdx) in self.registeredIslands:
                return
            
            # * Add the coords into the set for checking --> And valid coordinates into the set()
            self.registeredIslands.add((rowIdx,colIdx))

            """
            Traversal
            """
            # TODO: At this stage, no violations were found, that means either all island coordinates were inputted; or we are still traversing 
            # Right (Check bounds first, then content, then visited status)
            if colIdx + 1 < self.colLength and grid[rowIdx][colIdx + 1] == '1' and (rowIdx, colIdx + 1) not in self.registeredIslands:
                dfs(rowIdx, colIdx + 1)
            # Bottom 
            if rowIdx + 1 < self.rowLength and grid[rowIdx + 1][colIdx] == '1' and (rowIdx + 1, colIdx) not in self.registeredIslands: 
                dfs(rowIdx + 1, colIdx)
            # Left 
            if colIdx - 1 >= 0 and grid[rowIdx][colIdx - 1] == '1' and (rowIdx, colIdx - 1) not in self.registeredIslands: 
                dfs(rowIdx, colIdx - 1)
            # Top
            if rowIdx - 1 >= 0 and grid[rowIdx - 1][colIdx] == '1' and (rowIdx - 1, colIdx) not in self.registeredIslands:
                dfs(rowIdx - 1, colIdx)
            
            # Island count is incremented in the main loop when a new island is discovered

        # *=========================================================
        # Loop through the m x n grid now
        for row in range(self.rowLength):
            for col in range(self.colLength):
                if grid[row][col] == '1' and (row,col) not in self.registeredIslands:
                    self.islandCount += 1 # Found a new island
                    dfs(row, col)
        return self.islandCount
        

        
