from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        max_time = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append(((i,j),0))

        while len(q) > 0:
            (i,j),time = q.popleft()
            max_time = max(max_time,time)
            if i-1>= 0 and not visited[i-1][j] and grid[i-1][j] == 1:
                q.append(((i-1,j),time+1))
                visited[i-1][j] = True
            if i+1 <n and not visited[i+1][j] and grid[i+1][j] == 1:
                q.append(((i+1,j),time+1))
                visited[i+1][j] = True
            if j-1>= 0 and not visited[i][j-1] and grid[i][j-1] == 1:
                q.append(((i,j-1),time+1))
                visited[i][j-1] = True
            if j+1 <m  and not visited[i][j+1] and grid[i][j+1] == 1:
                q.append(((i,j+1),time+1))
                visited[i][j+1] = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1 

        return max_time

        



        