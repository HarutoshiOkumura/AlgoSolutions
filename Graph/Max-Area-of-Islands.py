from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        1. DFS to find the island, then append island size after
        2. Keep track of the max island size with an int var --> Global var. or not? 
        3. DFS directions of right, bottom, left, top 
        4. At each level, we check the current island size with the current largest, then return the largest island size at the end 
        5. Handle repeated '1' logic at the main function's for loop level 
        """

        self.registeredIslands = set()

        # =========================================
        def islandFinder(rowIdx, colIdx, islandSize):
            """
            Base cases 
                1) When the pointers are out of grid's bounds 
                2) When the current grid[rowIdx][colIdx] is out of bounds 
            """
            print("============================================")
            # To avoid null pointer referencing
            if rowIdx < 0 or colIdx < 0 or rowIdx >= len(grid) or colIdx >= len(grid[0]): 
                return 
            
            # To deal with cases == 0; to which we just return to the previous recursive depth 
            if (grid[rowIdx][colIdx] == 0):
                print(f"Current grid[{rowIdx}][{colIdx}] is 0, returning to previous recursive depth")
                return 
            

            # TODO: To catch cases that have already been registered: 
            if ((rowIdx,colIdx) in self.registeredIslands):
                print(f"Current grid[{rowIdx}][{colIdx}] has already been registered, returning to previous recursive depth")
                return 
            
            # * ================================    
            
            # ? If all the base cases are validated, it means that the current land, is a valid island piece to document 
            islandSize += 1 
            self.localCount += 1
            print(f"Island size updated to: {islandSize}")

            # TODO: Check the max island size right now at this snapshot 
            
            print(f"Max island size updated to: {self.localCount}")

            # TODO: Also need to add valid island to the registeredIslands list 
            self.registeredIslands.add((rowIdx, colIdx))
            print(f"Registered islands: {self.registeredIslands}")

    

            print(f"Starting to traverse in 4 directions with the current coordinates: {rowIdx}, {colIdx}")

            """
            Traversal - Right -> Bottom -> Left -> Top
            """
            # 1) Right
            print(f"Going Right to: {rowIdx}, {colIdx + 1}")
            islandFinder(rowIdx, colIdx + 1, islandSize)
            
            # 2) Bottom 
            print(f"Going Bottom to: {rowIdx + 1}, {colIdx}")
            islandFinder(rowIdx + 1, colIdx, islandSize)

            # 3) Left
            print(f"Going Left to: {rowIdx}, {colIdx - 1}")
            islandFinder(rowIdx, colIdx - 1, islandSize)

            # 4) Top
            print(f"Going Top to: {rowIdx - 1}, {colIdx}")
            islandFinder(rowIdx - 1, colIdx, islandSize)
        # =========================================
        finalCount = 0 
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[rowIdx])):
                # ! Check for repeated "1"s
                if ((rowIdx,colIdx) not in self.registeredIslands): 
                    # Reset the localCount to 0 for the next iteration 
                    self.localCount = 0
                    islandFinder(rowIdx, colIdx, self.localCount)
                    finalCount = max(self.localCount,finalCount)
                    


        return finalCount


        
