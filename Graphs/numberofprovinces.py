class Solution(object):
    def dfs(self,i,adj,vis):
        vis[i] = True
        for j in range(len(adj)):
            if adj[i][j] == 1 and not vis[j]:
                self.dfs(j,adj,vis)
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        number = 0
       
        n = len(isConnected)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                self.dfs(i,isConnected,visited)
                number += 1
        return number
                
        