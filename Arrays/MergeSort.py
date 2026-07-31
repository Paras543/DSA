class Solution(object):

    def merge(self,nums,start,mid,end):
        temp = []
        i = start
        j= mid + 1
        while(i<=mid and j<=end):
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while(i<=mid):
            temp.append(nums[i])
            i+=1

        while (j<=end):
            temp.append(nums[j])
            j +=1 

        for idx in range(len(temp)):
            nums[idx+start] = temp[idx]

    def mergesort(self,nums,start,end):
        if start < end:
            mid = start + (end-start)//2
            self.mergesort(nums,start,mid)
            self.mergesort(nums,mid+1,end)
            self.merge(nums,start,mid,end)




    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        self.mergesort(nums,0,len(nums)-1)

        return nums 
    

    