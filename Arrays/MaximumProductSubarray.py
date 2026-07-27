class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            old_max = max_product
            old_min = min_product
            new_min = min(num,old_max*num,old_min*num)
            new_max = max(num,old_max*num,old_min*num)
            max_product = new_max
            min_product = new_min

            answer = max(answer,new_max)

        return answer
           
          
            

            
            
     
            