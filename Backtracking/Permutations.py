class Solution(object):
    def getpermuations(self,nums,idx,ans):
        if idx == len(nums):
            ans.append(nums[:])
            return 

        
        

        for i in range(idx,len(nums)):
            nums[idx] , nums[i] = nums[i] , nums[idx]
            self.getpermuations(nums,idx+1,ans)
            nums[idx] , nums[i] = nums[i] , nums[idx]


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        self.getpermuations(nums,0,ans)
        return ans 
        
        