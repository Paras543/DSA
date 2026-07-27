class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxi = float('-inf')
        sum = 0 
        start = 0
        arr_start = 0
        arr_end = 0
        for i in range(len(nums)):
            
            sum += nums[i]
            if (sum>maxi):
                maxi = sum 
                arr_start = start
                arr_end = i
            if(sum<0):
                sum = 0
                start = i+ 1

            subarray = nums[arr_start:arr_end+1]
        return maxi,subarray




