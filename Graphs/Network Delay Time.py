import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n+1)]
        for u,v,wt in times:
            adj[u].append((v,wt))

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        pq = [(0,k)]

        while pq:
            d,u = heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,wt in adj[u]:
                new_dist = d + wt
                if new_dist <dist[v]:
                    dist[v] = new_dist
                    
                    heapq.heappush(pq,(new_dist,v))
        if max(dist[1:] ) == float("inf"):
            return -1
        return max(dist[1:])

