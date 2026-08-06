class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = n-1

        while r < m and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                target > matrix[r][c]
                r += 1

        return False



      
        