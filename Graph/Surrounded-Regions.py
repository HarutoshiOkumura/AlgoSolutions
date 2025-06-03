from collections import deque # Added import for deque
from typing import List # Ensure List is imported for type hinting

"""
Thoughts: 
    1) DFS or BFS? 
    2) WHen it comes to validating a singular 'O', I think there are only 3 rules: 
        a) If in any direction, there is an 'O', its ok 
        b) If in any direction there is 'X' that is ok; 
        c) All 4 direction must be surrounded 
    3) Obvious pickups: 
        a) If out of bound, then its clear that its not surrounded --> Actually is the only way 
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # Top, Right, Bottom, Left

        # Helper BFS function to mark 'O's connected to borders as safe ('#')
        def mark_safe_bfs(r, c):
            # Check if the starting point is valid and an 'O'
            # This initial check is mostly for safety, as calls from border loops should ensure it's 'O'
            if not (0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O'):
                return

            queue = deque([(r, c)])
            board[r][c] = '#' # Mark the initial border 'O' as safe

            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    # Check for bounds and if the neighbor is an 'O' (not yet marked safe)
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O':
                        board[nr][nc] = '#' # Mark it as safe
                        queue.append((nr, nc))

        # Step 1: Mark all 'O's connected to the border as safe ('#')
        # Iterate over top and bottom rows
        for c_idx in range(COLS):
            if board[0][c_idx] == 'O':
                mark_safe_bfs(0, c_idx)
            if ROWS > 1 and board[ROWS - 1][c_idx] == 'O': # Ensure ROWS > 1 for distinct last row
                mark_safe_bfs(ROWS - 1, c_idx)

        # Iterate over left and right columns (excluding corners already covered by row iteration)
        for r_idx in range(1, ROWS - 1): # from 1 to ROWS-2
            if board[r_idx][0] == 'O':
                mark_safe_bfs(r_idx, 0)
            if COLS > 1 and board[r_idx][COLS - 1] == 'O': # Ensure COLS > 1 for distinct last col
                mark_safe_bfs(r_idx, COLS - 1)

        # Step 2: Flip remaining 'O's to 'X' and safe '#' back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X' # These 'O's were not reached from a border
                elif board[r][c] == '#':
                    board[r][c] = 'O' # These were the safe 'O's
        # No return needed as board is modified in-place

        