from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        
        adj = [[] for _ in range(n)]

        for u,v,wt in flights:
            adj[u].append((v,wt))
        dist = [float("inf")] * n
        dist[src] = 0

        q = deque([(src,0,-1)])

        while q:
            u,cost,stops = q.popleft()
            if stops == k:
                continue
            for v,wt in adj[u]:
                new_cost = cost + wt
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    q.append((v, new_cost, stops + 1))

        return -1 if dist[dst] == float("inf") else dist[dst]

           

