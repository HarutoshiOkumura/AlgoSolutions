from typing import List 
from collections import deque
"""
Time Complexity Explanation:
- Naive DFS (from each empty cell): O((m*n)^2) - Like many painters starting from different empty rooms, each potentially re-painting the whole grid (m*n rooms) if they find a gate. (m*n) starts * (m*n) work/start.
- Multi-Source BFS (from all gates): O(m*n) - Like dye spreading from all gates simultaneously. Each room is 'colored' (visited and processed) with its shortest distance once. Each of m*n rooms is enqueued/dequeued once, and its (at most 4) neighbors are checked.
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = []
        queue = deque() # * Append(insertion from left) and pop(removal from right) to maintain FIFO validity 
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0]) if rooms else (0,0)
        if rows == 0 or cols == 0:
            return

        # TODO: Nested for-loop to find ALLL the GATES first 
        for rowIdx in range(len(rooms)): 
            for colIdx in range(len(rooms[rowIdx])): 
                if (rooms[rowIdx][colIdx] == 0):
                    # Append zero as all gates have 0 distance from themselves
                    gates.append((0,rowIdx,colIdx))
        # print(f"These are all the gates after 1st pass: {gates}")

     
        def multiBFS(gates_list): # Renamed gates to gates_list to avoid conflict with outer scope if any confusion
            # TODO: Start looping until the queue is empty --> No more nodes to process == we are done! 
            while queue: 
                # ! Remember that we are peeling layer by layer
                print("=============================")
                # dist_to_current_node is the actual distance from a gate to (rowIdx, colIdx)
                dist_to_current_node, rowIdx, colIdx = queue.popleft()
                print(f"Current queue: {queue}, just popped node: ({dist_to_current_node}, {rowIdx}, {colIdx})")

                # Base Cases for the POPPED node (rowIdx, colIdx)
                # * 1) When the indices are out of bounds (should ideally not happen if checks are done before adding)
                if not (0 <= rowIdx < rows and 0 <= colIdx < cols):
                    print(f"Indices {rowIdx, colIdx} are out of bounds (from queue), skipping this node")
                    continue

                # * 2) If the square is a wall (should ideally not happen if checks are done before adding)
                if rooms[rowIdx][colIdx] == -1: 
                    print(f"Node {rowIdx, colIdx} is a wall (from queue), skipping this node")
                    continue

                # ! 3) If we found a shorter path to rooms[rowIdx][colIdx] already and this queue entry is stale.
                #    (Or, if it's a gate, dist_to_current_node should be 0, rooms[rowIdx][colIdx] is 0, so 0 > 0 is false)
                if dist_to_current_node > rooms[rowIdx][colIdx]:
                    print(f"Node {rowIdx, colIdx} with dist {dist_to_current_node} is suboptimal path (rooms[{rowIdx}][{colIdx}]={rooms[rowIdx][colIdx]}), skipping.")
                    continue
                
                # At this point, (dist_to_current_node, rowIdx, colIdx) is a valid state to process.
                # rooms[rowIdx][colIdx] is either 0 (gate) or has been updated by a previous shorter/equal path, or is INF.
                # If rooms[rowIdx][colIdx] was INF, it should be updated by the value that caused it to be enqueued.
                # This means rooms[rowIdx][colIdx] should already be <= dist_to_current_node. The check above handles if it's stale.
                # The problem's description of INF implies we fill it. The assignment rooms[next_r][next_c] = dist_for_neighbor (below) handles this.

                # Calculate the distance for neighbors of the current node
                dist_for_neighbors = dist_to_current_node + 1

                # Define relative coordinates for neighbors: Top, Right, Bottom, Left
                neighbor_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

                for dr, dc in neighbor_directions:
                    next_r, next_c = rowIdx + dr, colIdx + dc

                    # Check 1: Is the neighbor within bounds?
                    if not (0 <= next_r < rows and 0 <= next_c < cols):
                        continue
                    
                    # Check 2: Is the neighbor a wall?
                    if rooms[next_r][next_c] == -1:
                        continue

                    # Check 3: Is this new path to the neighbor shorter than any existing path?
                    if dist_for_neighbors < rooms[next_r][next_c]:
                        # Shorter path found, update the room's distance and add to queue
                        print(f"  Updating neighbor ({next_r}, {next_c}): old_dist={rooms[next_r][next_c]}, new_dist={dist_for_neighbors}")
                        rooms[next_r][next_c] = dist_for_neighbors
                        queue.append((dist_for_neighbors, next_r, next_c))
                    print(f"  Neighbor ({next_r}, {next_c}) not updated: rooms_val={rooms[next_r][next_c]}, new_dist={dist_for_neighbors}")
            
        
        # TODO: Then run the multiBFS -> Layer by layer -> Pass in the roots so that we can iteratively find go down the entire tree
        print(f"About to run multiBFS")
        # ! When first passed into the function -> We will deal with the roots first, which are the nodes inside of gates 
        for root_gate_info in gates: # gates contains (0, r, c)
            # root_gate_info is (initial_dist, r, c)
            # The distance in rooms[r][c] for a gate is already 0. We queue it with this distance.
            queue.append(root_gate_info) 
        print(f"Just queued up all the root nodes (all gates): {queue}, about to start BFS")
        multiBFS(gates)
        # return rooms # Modified in-place