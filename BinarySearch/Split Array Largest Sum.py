class Solution(object):
    def check_minimum(self,nums,max_allowed_sum):
        subarray = 1
        sum = 0

        for i in range(len(nums)):
            if sum + nums[i] <= max_allowed_sum:
                sum += nums[i]

            else:
                subarray += 1
                sum = nums[i]

        return subarray




    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start = max(nums)
        end = sum(nums)
        ans = start


        while start <= end:
            mid = start + (end-start)//2
            minimized_sum = self.check_minimum(nums,mid)

            if minimized_sum <= k :
                ans = mid 
                end = mid - 1
            else:
                start = mid + 1

        return ans





        

        