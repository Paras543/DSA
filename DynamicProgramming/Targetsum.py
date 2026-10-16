class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        total = sum(nums)
        if abs(target)> total:
            return 0
        if (target+total) % 2 != 0:
            return 0
        subset_sum = (target+total)//2

        dp = [0]*(subset_sum+1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum,num-1,-1):
                dp[j] += dp[j-num]
        return dp[subset_sum]