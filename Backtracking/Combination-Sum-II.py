from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def dfs (idx: int, curr: List[int], currSum):
            if (currSum == target): 
                answer.append(curr.copy())
                return 
            if (currSum > target) or (idx >= len(candidates)):
                return 
            
            curr.append(candidates[idx])

            # Left split: First Decision to append new element indexed by idx
            dfs(idx + 1 , curr, currSum + candidates[idx])

            # Revert to parent node, so that it can be processed by the right split 
            curr.pop()

            # Right split: Second Decision to not append anything and keep the original 
            dfs(idx, curr, currSum)
        dfs(0, [], 0)
        return answer

