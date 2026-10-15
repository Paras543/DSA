class Solution(object):

    def helper(self, nums, st, end):
        n = end - st + 1
        dp = [0] * n

        if n == 1:
            return nums[st]

        dp[0] = nums[st]
        dp[1] = max(nums[st], nums[st + 1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[st+i])

        return dp[n-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        return max(self.helper(nums, 0, n-2),
                   self.helper(nums, 1, n-1))