class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        my_map = {}
        my_map[0] = 1
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            prefix_sum += num

            remove = prefix_sum - k
            count += my_map.get(remove,0)
            my_map[prefix_sum] = my_map.get(prefix_sum, 0) + 1

        return count

            
            
## approach is that like go in the array find out the prefix sum and find the remove which is basically the complememnt 
## the count is increased by if it sees the same element in the hashmap
## and if the prefix sum is seen more than once then we update it 
