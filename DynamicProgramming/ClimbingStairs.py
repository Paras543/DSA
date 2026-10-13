class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [0] * (n+1)
        dp[1] = 1
        if n>=2 :
            dp[2] = 2

        for i in range(3,len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
