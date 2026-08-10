class Solution(object):
    def combsum(self,candidates,i,combinations,ans,target):
        if target == 0 :
            ans.append(combinations[:])
            return
        if i == len(candidates) or target < 0:
            return

        combinations.append(candidates[i])
      
        self.combsum(candidates,i,combinations,ans,target - candidates[i])
        combinations.pop()
        self.combsum(candidates,i+1,combinations,ans,target)





    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []

        ans = []
        self.combsum(candidates,0,combinations,ans,target)
        return ans


      

      