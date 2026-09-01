class Solution(object):
    def dfs(self,i,j,vis,grid,n,m):
        if i <0 or j <0 or i>= n or j >= m or vis[i][j] or grid[i][j] != '1':
            return 
        vis[i][j] = True
        self.dfs(i-1,j,vis,grid,n,m)
        self.dfs(i,j+1,vis,grid,n,m)
        self.dfs(i+1,j,vis,grid,n,m)
        self.dfs(i,j-1,vis,grid,n,m)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not vis[i][j]:
                    self.dfs(i,j,vis,grid,n,m)
                    islands += 1
        return islands
        