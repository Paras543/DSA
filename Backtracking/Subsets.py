class Solution(object):
    def allsubstes(self,nums,ans,i,all_subsets):
        if i == len(nums):
            all_subsets.append(ans[:])

            return 

        ans.append(nums[i])
        self.allsubstes(nums,ans,i+1,all_subsets)
        ans.pop()
        self.allsubstes(nums,ans,i+1,all_subsets)



    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_subsets = []
        ans = []
        self.allsubstes(nums,ans,0,all_subsets)

        return all_subsets

       

        

        