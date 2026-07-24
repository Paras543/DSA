class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1 
        maximum_area = 0


        while l < r:
            width = r - l
            area = width * min(height[l],height[r])
            
            maximum_area = max(maximum_area,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        

        return maximum_area