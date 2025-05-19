class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        ds = []
        candidates.sort()
        """
        # Sorted = [1,1,2,5,6,7,10]
        """

        def findCombination(index, target):
            # Base case
            if target == 0:
                ans.append(ds.copy()) # ds[:] creates a copy/slice of the entire list to avoid appending a reference
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombination(i + 1, target - candidates[i])
                ds.pop()


        findCombination(0, target)  
        return ans