#from typing import List
#from Collections import deque

"""
Thoughts: 
    1) I'm imagining that the code will be to represent the rotting phenomenom, then return: 
        a) Number of loops needed to complete the rotting 
        b) Even if the rotting completes, if there are still oranges left, then we will still have to return -1 to indicate failure in rotting 
    2) 4-directional adjacent traversal -> BFS spreading 
    3) Assume multiple oranges can be rotten at the initial stage -> Multi-source shortest path (time-wise) 
"""
"""
Structs: 
    1) @param time: time represent time which is each layer of BFS
    2) def rottingBFS: to represent how rotting happens 
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        initialRots = [] # ! I know that queue is all I need, but using initialRots to separate the logic is clearer for me 
        queue = deque()
        directions = [(-1,0),(0,1),(1,0),(0,-1)] # Top -> Right -> Bottom -> Left
        visitedOranges = set()
        totalOranges = 0
        totalRotten = 0
        layer = 0
        

        # TODO: Find all the initially rotten oranges first 
        for rowIdx in range(len(grid)): 
            for colIdx in range(len(grid[rowIdx])):
                # 2 to represent that they are rotten already
                # ! We need to count the number of oranges here, so that we can use the difference between all organes and infected oranges to see if we have attained what we want 
                if (grid[rowIdx][colIdx] != 0): 
                    totalOranges += 1
                
                # TO track all the oranges that are set
                if (grid[rowIdx][colIdx] == 2):
                    # * Append their indices for tracking 
                    initialRots.append((rowIdx,colIdx,0)) # ! 0 to keep track of the layer of spreadage
        print(f"Initial Rots: {initialRots}")
        print(f"Total Oranges: {totalOranges}")
        if (totalOranges == 0):
            return 0
        print("================================================")
        # * ===================================================================================================================
        # # TODO: Then kickstart the rotting with the initially rotten oranges as starting points --> BFS your way through it 
        for rots in initialRots:
            queue.append(rots)
            totalRotten += 1
        print(f"Total Rotten after pushing into queue initially : {totalRotten}")
        print("================================================")
        # *=====================================================================

        # TODO: Start of the multi-source BFS
        print(f"About to start BFS with queue: {queue}")
        while queue: 
            print(f"================================================")
            print(f"Current loop deals with the orange: {queue[0]}")
            rowIdx, colIdx, layer = queue.popleft()
            print(f"Current Orange {rowIdx, colIdx} is being popped from queue, layer: {layer}")
            # TODO: Check the base cases that requires indexing 

            # !If the number of rotten oranges matches the total number of oranges then we are set 
            print(f"Current Total Rotten: {totalRotten}")
            print(f"Current Total Oranges: {totalOranges}")

            # !===========
            # ! This is the main culprit of the bug RIGHT NOW
            #!===========
            if (totalOranges == totalRotten): 
                return layer

            # 3) If the current orange is healthy == 1, then we have to infect them
            if (grid[rowIdx][colIdx] == 1):
                print(f"Current Orange {rowIdx, colIdx} is healthy, infecting...")
                grid[rowIdx][colIdx] = 2
                totalRotten += 1 
                print(f"Current Total Rotten after infecting: {totalRotten}")

            # * Dealing with the current orange 
            
            visitedOranges.add((rowIdx,colIdx))
            print(f"Current Visited Oranges: {visitedOranges}")
            
            # TODO: Dealing with traversing to the neighboring oranges, which means their layer is + 1 
            layer += 1 

            # !Iterate through all 4 directions: 
            for dr, dc in directions: 
                print(f"Current Direction: {dr, dc}")
                newRow, newCol = rowIdx + dr, colIdx + dc
                if not (0 <= newRow < len(grid) and 0 <= newCol < len(grid[newRow])):
                    continue
                if (grid[newRow][newCol] == 0):
                    print(f"Current Orange {newRow, newCol} is an empty cell {grid[newRow][newCol]}, skipping...")
                    continue
                if ((newRow, newCol) in visitedOranges):
                    print(f"Current Orange {newRow, newCol} has already been visited, skipping...")
                    continue
                # Layer here has been +1-ed
                # If they are no out of bounds, then we can explore the next oranges
                queue.append((newRow, newCol, layer))
                print(f"Current Orange {newRow, newCol} is being pushed into queue, layer: {layer}")
            print(f"What queue looks like after the current loop: {queue}")
        
        return -1
            
        


