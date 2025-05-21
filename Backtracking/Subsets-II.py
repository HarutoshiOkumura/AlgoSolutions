from typing import List

"""
Problem Statement - This problem is NOT asking for the power set of a set. It is asking for all, sorted, unique combinations of the terms in the input.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

"""
Questions to address
"""
# ! 1) Is the inputed sorted? If yes, then just take out the sorting algo 


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        ds = []

        def backTracking(currentIdx): 
            print(f"Current ds at the top of new backTracking layer: {ds}")
            # Base case for faulty nodes 
            if (currentIdx > len(nums)): 
                print(f"Base error validated with currentIdx: {currentIdx} >= {len(nums)}")
                return 
            # If nothing is faulty then append 
            ans.append(ds.copy())
            print(f"New answer appended: {ds.copy()}")
            # Then return for the case where we reached max length 
            if (len(ds) == len(nums)):  
                print(f"Max length approached at: {ds}")
                return 
            
            # Recursion 
            for i in range(currentIdx, len(nums)):
                # Explanation for skipping duplicates:
                #! `nums` is sorted, so identical elements are grouped together.
                #? The loop `for i in range(currentIdx, len(nums))` considers elements starting from `nums[currentIdx]`.
                #
                #! The condition `(i > currentIdx and nums[i] == nums[i - 1])` (on the next line) is designed to avoid duplicate subsets.
                #? - `nums[i] == nums[i - 1]`: Checks if the current element is a duplicate of the previous one.
                #! - `i > currentIdx`: This is crucial. It means that we are NOT at the first element (`nums[currentIdx]`)
                #   that this particular recursive call is considering from the `nums` array for the current branch.
                #   Instead, we are at `nums[currentIdx+1]`, `nums[currentIdx+2]`, etc., within the same `for` loop.
                #
                #? Why skip (when the condition on the next line is true)?
                #! If `i > currentIdx`, it implies `nums[i-1]` was a candidate considered in the *current* `for` loop\'s
                # previous iteration (since `i-1 >= currentIdx`).
                #! If `nums[i]` is identical to `nums[i-1]`, then any subsets formed by choosing `nums[i]` at this stage
                # (and then recursing) would be duplicates of subsets already generated when `nums[i-1]` was chosen
                # in the previous loop iteration (followed by its recursive calls).
                #
                #? Example: nums = [1,2,2,2], currentIdx = 0. Outer call `backTracking(0)`.
                #   - First, `[]` is added.
                #   - Loop i from 0:
                #     - i = 0 (nums[0]=1): Pick 1. ds=[1]. Call backTracking(1).
                #       - Inside backTracking(1) (currentIdx=1, ds=[1]):
                #         - Add [1] to ans.
                #         - Loop j from 1 (currentIdx for this inner call):
                #           - j = 1 (nums[1]=2): `j > currentIdx` (1 > 1) is false. Pick nums[1]. ds=[1,2]. Call backTracking(2).
                #             - Inside backTracking(2) (currentIdx=2, ds=[1,2]):
                #               - Add [1,2] to ans.
                #               - Loop k from 2:
                #                 - k = 2 (nums[2]=2): `k > currentIdx` (2 > 2) is false. Pick nums[2]. ds=[1,2,2]. Call backTracking(3).
                #                   - ... this adds [1,2,2] and [1,2,2,2] if nums was [1,2,2,2]
                #                 - k = 3 (nums[3]=2, if present): `k > currentIdx` (3 > 2) true. nums[3]==nums[2] true. Skip.
                #           - j = 2 (nums[2]=2): `j > currentIdx` (2 > 1) true. nums[2]==nums[1] true. Skip.
                #             (This prevents forming [1, (second 2), ...] when [1, (first 2), ...] already covered it)
                #     - i = 1 (nums[1]=2): `i > currentIdx` (1 > 0) true. nums[1]==nums[0] (2==1) false. Pick 2. ds=[2]. Call backTracking(2).
                #       - ...This branch generates [2], [2,2], [2,2,2]
                #     - i = 2 (nums[2]=2): `i > currentIdx` (2 > 0) true. nums[2]==nums[1] (2==2) true. Skip.
                #       (This prevents starting a new top-level branch with the second '2' if nums was [1,2,2] or [2,2,...])
                #
                #! In essence, for any given level of recursion and its `for` loop, when encountering a sequence
                # of identical numbers, we only allow the *first* of these identical numbers encountered in that loop
                # (i.e., when `i == currentIdx`, or when `nums[i] != nums[i-1]`) to start a new path of subset generation.
                #! This prevents generating the same subset multiple times by starting with different-but-identical elements.
                if (i > currentIdx and nums[i] == nums[i - 1]):
                    continue
                # Action 
                ds.append(nums[i])

                # backtrack 
                backTracking(i + 1)

                # backtrack the action to explore the next option 
                ds.pop()
            
        backTracking(0)
        return ans

            

