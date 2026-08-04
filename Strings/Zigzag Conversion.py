class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        rows = [""] * numRows
        current_row = 0
        direction = 1
        

        if numRows == 1:
            return s 

        for ch in s:
            rows[current_row] += ch
            if current_row == 0:
                direction = 1
            

            if current_row == numRows-1:
                direction = -1

            current_row += direction
            

        
        return "".join(rows)

            
            


            



        
