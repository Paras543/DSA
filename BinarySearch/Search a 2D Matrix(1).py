class Solution(object):

    def searchinRow(self,matrix,target,row):
        n = len(matrix[0])
        start = 0
        end = n-1
        while start <= end:
            mid = start + (end-start)/2
            if target == matrix[row][mid]:
                return True
            elif target >= matrix[row][mid]:
                start = mid + 1
            else:
                end = mid -1

        return False

    

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0]) 
        startRow = 0
        endRow = m-1

        while startRow <= endRow:
            midRow = startRow + (endRow-startRow)/2

            if target >= matrix[midRow][0] and target<=matrix[midRow][n-1]:
                return self.searchinRow(matrix,target,midRow)

            elif target >= matrix[midRow][n-1]:
                startRow = midRow + 1
            else:
                endRow = midRow - 1



        return False





        