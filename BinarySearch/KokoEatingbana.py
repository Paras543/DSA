
class Solution(object):
    def requriedTime(self,piles,hourly):
        total_hours = 0
        for pile in piles:
            total_hours += (pile + hourly - 1) // hourly

        return total_hours

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = low + (high-low)//2
            total_hours = self.requriedTime(piles,mid)
          
        
            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 

        return ans


        
        