class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        arrows = 1
        arrows_pos = points[0][1]

        for i in range(1,len(points)):
            if points[i][0] > arrows_pos:
                arrows += 1
                arrows_pos = points[i][1]
        return arrows

