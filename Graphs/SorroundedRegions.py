class Solution(object):
    def dfs(self,i,j,visited,board,n,m,region):
        if i<0 or j<0 or i>=n or j>=m:
            return False
        if visited[i][j] or board[i][j] != 'O':
            return False
        visited[i][j] = True
        region.append([i,j])
        touches_boundary = (
            i == 0 or i==n-1 or j==0 or j==m-1

        )

        if self.dfs(i-1,j,visited,board,n,m,region):
            touches_boundary = True
        if self.dfs(i+1,j,visited,board,n,m,region):
            touches_boundary = True
        if self.dfs(i,j-1,visited,board,n,m,region):
            touches_boundary = True
        if self.dfs(i,j+1,visited,board,n,m,region):
            touches_boundary = True
        return touches_boundary


    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    region = []

                    touches_boundary = self.dfs(i,j,visited,board,n,m,region)

                    if not touches_boundary:
                        for x,y in region:
                            board[x][y] = 'X'