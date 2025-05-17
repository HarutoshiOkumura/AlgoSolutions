from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(idx: int, curr: List[int], sumSoFar): 
            # TODO: Base cases first 
            # 1. If the correct case is found 
            if (sumSoFar == target): 
                answer.append(curr.copy())
                return 
            # 2. Overflow case where the sum too big OR we out of bounds
            if (sumSoFar > target) or (idx >= len(candidates)): 
                return 
            
            # TODO: The 2 Decisions to make for backTracking
            # ! Adding the current idx, first renew the list and target to for checking purposes and to pass it into the next round
            curr.append(candidates[idx])

            dfs(idx, curr, sumSoFar + candidates[idx])
            # ! Pop to backtrack for the for the right child
            curr.pop()

            dfs(idx + 1, curr, sumSoFar)
        dfs(0, [], 0)
        return answer