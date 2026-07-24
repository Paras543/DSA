class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l =0
        r =len(height) - 1
        left_max =0 
        right_max = 0
        total_water = 0
        while l < r:
            left_max = max(left_max,height[l])
            right_max = max(right_max,height[r])
            
            if left_max <= right_max:
                trapped_water = left_max - height[l]
                l +=1
            else:
                trapped_water = right_max - height[r]
                r -= 1



            
            total_water = trapped_water + total_water

        return total_water

