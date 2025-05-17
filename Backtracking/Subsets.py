"""
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
from typing import List

"""
? Why Backtracking in this problem of finding the powersets? 

! Characteristics of backtracking 
    1. You build a solution step by step -> adding one decision at a time (In this case, it is whether to inluce or exlucde the new thing) 
        ! a) We could formulate the problem as a sequence of choices 
    2. At each decision step, you have two possible choice that will elad down to different branches of search 
    3. After DFS exploring one branch, you undo one step to explore the next branch 
    4. Recording the leaf nodes as the complete answer
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subset = []

        def backtrack(index: int):
            # Base case: if we have considered all numbers in nums
            # e.g., if nums=[1,2] and index becomes 2, we've made decisions for 1 and 2.
            if index >= len(nums):
                answer.append(subset.copy()) # Add a copy of the current subset to the answer
                # Example: if subset is [1,2], answer becomes [[1,2]] (if it was empty)
                # Example: if subset is [1], answer becomes [..., [1]]
                # Example: if subset is [], answer becomes [..., []]
                return

            # Decision 1: Include nums[index] in the current subset
            # e.g., if nums=[1,2], index=0 (current num is 1). subset is initially [].
            # After append, subset becomes [1].
            current_num = nums[index]
            subset.append(current_num)
            # Recursively call backtrack for the next number.
            # e.g., backtrack(1) is called with subset=[1].
            backtrack(index + 1)

            # Decision 2: Exclude nums[index] from the current subset (Backtrack step)
            # This happens after the above backtrack(index + 1) call returns.
            # We need to remove the current_num to explore paths where it's not included.
            # e.g., if subset was [1] (after including 1 and its subsequent calls returned),
            # .pop() makes subset [].
            # e.g., if subset was [1,2] (after including 1, then 2, and its calls returned),
            # .pop() makes subset [1].
            subset.pop()
            # Recursively call backtrack for the next number, but without current_num in the subset.
            # e.g., if nums=[1,2], index=0. After 1 was included and then popped, subset is [].
            # backtrack(1) is called with subset=[].
            backtrack(index + 1)

        backtrack(0) # Start the recursion from the first number (index 0)
        return answer
    

# Example usage (optional, for testing):
# sol = Solution()
# print(sol.subsets([1,2,3]))
# print(sol.subsets([0]))
            