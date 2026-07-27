class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        temp_start = 0
        arr_start = 0
        arr_end = 0

        for i in range(1, len(nums)):
            num = nums[i]

            old_max = max_product
            old_min = min_product

            
            if num > max(old_max * num, old_min * num):
                max_product = num
                min_product = num
                temp_start = i
            else:
                max_product = max(old_max * num, old_min * num)
                min_product = min(old_max * num, old_min * num)

            if max_product > answer:
                answer = max_product
                arr_start = temp_start
                arr_end = i

        return nums[arr_start:arr_end + 1]