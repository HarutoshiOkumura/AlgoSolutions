from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        ds = []
        def backTracking(currentIdx, currentPos):
            # Base case, the array sizes match
            if len(ds) == len(nums): 
                answer.append(ds.copy())
                print(f"Answers obtained: {ds.copy()}")
                return 
            if currentIdx >= len(nums): 
                print(f"Overflow at index: {currentIdx}")
                return 

            for idx in range(len(ds) + 1):
                print(f"New loop at depth {currentIdx} with idx {idx}")
                ds.insert(idx, nums[currentIdx])

                print(f"Post insertion of {nums[currentIdx]} at {currentPos}, result: {ds}")
                # currentPos should be in sync with the amount of loops
                print(f"New backTrack layer at index: {currentIdx + 1}")
                backTracking(currentIdx + 1, idx)
                # Pop to continuously inserting and reinserting
                print(f"Removed {nums[currentIdx]} from {ds}")
                ds.pop(idx)
        backTracking(0, 0)
        return answer


            

