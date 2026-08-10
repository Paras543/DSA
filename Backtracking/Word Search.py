class Solution(object):
    def gridsearch(self,board,word,row,col,idx):
        if idx == len(word):
            return True

        if row <  0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[idx]:
            return False

        temp = board[row][col]
        board[row][col] = '#'
        found = (
            self.gridsearch(board,word,row+1,col,idx+1) or
            self.gridsearch(board,word,row-1,col,idx+1) or
            self.gridsearch(board,word,row,col+1,idx+1) or 
            self.gridsearch(board,word,row,col-1,idx+1) 

        ) 

        board[row][col] = temp

        return found





     

    



    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.gridsearch(board,word,i,j,0) :
                        return True

        return False

                


