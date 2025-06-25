class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Optimal Solution: DP
        """
        """
        Input: cost = [10,15,20]
        Output: 15

        We know that at 20, it will take 20 only
        At 15, it can either go 20 or the end 
        At 10, it can either go 15 or 20 --> 1) 10 + 15 or 2) 10 + 20 
        """

        # TODO: Append 0 to the cost[] to indicate len(cost) + 1 as the landing point / top of the staircase 
        cost.append(0)
        print(f"cost[] before DP-ing: {cost}")
        # TODO: Now start at the position len(cost) - 1, aka the third last position to run DP
        # * Bottom up DP
        for step in range(len(cost) - 3, -1, -1): 
            print(f"cost[step]: {cost[step]}")
            print(f"cost[step + 1]: {cost[step + 1]}")
            print(f"cost[step + 2]: {cost[step + 2]}")
            cost[step] = cost[step] + min(cost[step + 1], cost[step + 2])
            print(f"cost[] after DP-ing: {cost} at step: {step}")
        print(f"cost[] after DP-ing: {cost}")
        print("============== Final Layer ===============")
        print(f"Final verdict: {min(cost[0], cost[1])}")
        # TODO: Return the smaller cost[0] vs cost[1]
        return min(cost[0], cost[1])