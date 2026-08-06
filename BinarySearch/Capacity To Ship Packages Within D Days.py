class Solution(object):

    def daysReuqired(self,weights,capacity):
        days = 1
        current_load = 0
        
        for weight in weights:
            if current_load + weight <= capacity:
                current_load += weight
            else: 
                days += 1
                current_load = weight
        return days


    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)
        ans = low

        while low <= high:
            mid = low + (high-low)//2
            total_days = self.daysReuqired(weights,mid)
            if total_days <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                

        return ans





             
            
        
        