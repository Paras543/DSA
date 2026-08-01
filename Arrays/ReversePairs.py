class Solution(object):

    def __init__(self):
        self.count = 0

    def merge(self, nums, start, mid, end):
        temp = []

        i = start
        j = mid + 1

        while i <= mid:
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            self.count += j - (mid + 1)
            i += 1

        i = start
        j = mid + 1

        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= end:
            temp.append(nums[j])
            j += 1

        for idx in range(len(temp)):
            nums[start + idx] = temp[idx]

    def mergesort(self, nums, start, end):
        if start < end:
            mid = start + (end - start) // 2
            self.mergesort(nums, start, mid)
            self.mergesort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)

    def reversePairs(self, nums):
        self.count = 0
        self.mergesort(nums, 0, len(nums) - 1)
        return self.count


        


        