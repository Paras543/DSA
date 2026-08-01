##With the optimal solution beacuse we are using here dutch national flag algorithm  + quick sort partiton index


import random
class Solution(object):

    def quickselect(self, nums, start, end, target):
        if start <= end:

            pivot = nums[random.randint(start, end)]

            low = start
            mid = start
            high = end

            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1


                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1

                else:
                    mid += 1

            if target < low:
                return self.quickselect(nums, start, low - 1, target) 

            elif target > high:
                return self.quickselect(nums, high + 1, end, target) 

            else:
                return nums[target]
            



    def findKthLargest(self, nums, k):
        target = len(nums) - k
        return self.quickselect(nums, 0, len(nums)-1, target)