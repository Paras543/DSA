class Solution(object):
    def dfs(self,i,j,visited,heights,n,m):
        if i<0 or j <0 or i>=n or j>=m or visited[i][j]:
            return 
        visited[i][j] =True

        if i>0 and heights[i-1][j]>=heights[i][j]:
            self.dfs(i-1,j,visited,heights,n,m)
        if i<n-1 and heights[i+1][j] >= heights[i][j]:
            self.dfs(i+1,j,visited,heights,n,m)
        if j>0 and heights[i][j-1] >= heights[i][j]:
            self.dfs(i,j-1,visited,heights,n,m)
        if j<m-1 and heights[i][j+1] >= heights[i][j]:
            self.dfs(i,j+1,visited,heights,n,m)






    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        

        n = len(heights)
        m = len(heights[0])

        pacific = [[False]*m for _ in range(n)]
        atlantic = [[False]*m for _ in range(n)]

        for j in range(m):
            self.dfs(0,j,pacific,heights,n,m)
        for i in range(n):
            self.dfs(i,0,pacific,heights,n,m)
        
        for j in range(m):
            self.dfs(n-1,j,atlantic,heights,n,m)
        for i in range(n):
            self.dfs(i,m-1,atlantic,heights,n,m)
        result = []

        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])
        return result
    

    