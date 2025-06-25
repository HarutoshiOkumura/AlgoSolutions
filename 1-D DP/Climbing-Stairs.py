class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the DP first 
        dp = [1] * (n + 1)
        print(f"Initialdp: {dp}")

        # Then we bottom up from the last two stair climbing

        for currStep in range(n - 2, -1, -1):
            print(f"Current dp: {dp} at step: {currStep}")
            # We start from the third last stair; and add the last and second last stairs' memoitized value 
            dp[currStep] = dp[currStep + 1] + dp[currStep + 2]
            print(f"Operation: dp[{currStep}] = dp[{currStep + 1}] + dp[{currStep + 2}]")
            print(f"Updated dp: {dp} at step: {currStep}")
        print(f"Final dp: {dp}")
        return dp[0]

