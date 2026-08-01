### With the Brute Force. solution beacuse we are taking the whole array and sorting it.
class Solution(object):
    def quickselect(self,nums,start,end,target):
        if start <= end:
            pivot_index = self.partition(nums,start,end)
         
        
            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index < target:
                return self.quickselect(nums,pivot_index+1,end,target)
            
            else:
                return self.quickselect(nums,start,pivot_index-1,target)
      

    def partition(self,nums,start,end):
        import random

        random_index = random.randint(start, end)
        nums[random_index], nums[end] = nums[end], nums[random_index]

        
        idx = start-1 
        pivot = nums[end]
        for j in range(start,end):
            if nums[j] <= pivot:
                idx += 1
                nums[j],nums[idx] = nums[idx],nums[j]
        idx += 1
        nums[end],nums[idx] = nums[idx],nums[end]
        return idx

    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = len(nums) - k

        return self.quickselect(nums,0,len(nums)-1,target)

        
        

