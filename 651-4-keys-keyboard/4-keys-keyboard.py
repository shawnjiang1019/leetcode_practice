class Solution:
    def maxA(self, n: int) -> int:
        # let dp[i] represnt the max number of A's after i keystrokes
        dp = [i for i in range(n + 1)]
        
        for i in range(4, n + 1):
            for k in range(i - 2):
                dp[i] = max(dp[i], dp[k] * (i - k - 1))
            dp[i] = max(dp[i], dp[i - 1] + 1)
        return dp[-1]
