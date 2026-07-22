class Solution(object):

    def store_values(self,nums):
        
        s = set()
        for i in nums:
            s.add(i)
        return s


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = self.store_values(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                current = num
                
                length = 1
                
                while current + 1 in s:
                    
                    current += 1 
                    length += 1

                longest = max(longest,length)

                

        return  longest



       

        
     
       


