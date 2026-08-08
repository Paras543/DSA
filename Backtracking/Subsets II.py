class Solution(object):
    def allsubstes(self,nums,ans,i,all_subsets):
        if i == len(nums):
             all_subsets.append(ans[:])
             return 
        ans.append(nums[i])
        self.allsubstes(nums,ans,i+1,all_subsets)
        ans.pop()

        idx = i + 1
        while idx < len(nums) and nums[idx] == nums[idx-1]:
            idx += 1

        self.allsubstes(nums,ans,idx,all_subsets)




    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        all_subsets = []
        ans = []

        self.allsubstes(nums,ans,0,all_subsets)

        return all_subsets
    
    