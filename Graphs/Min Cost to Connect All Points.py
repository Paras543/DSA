import heapq
class Solution(object):
    def manhatt(self,points,p1,p2):
        return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1]-points[p2][1])

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        pq = [(0,0)]
        mst_set = [False] * n
        mst_weight = 0
        count = 0
        while pq and count<n:
            weight,v = heapq.heappop(pq)
            if mst_set[v]:
                continue
            mst_set[v] = True
            mst_weight += weight
            count += 1

            for u in range(n):
                if not mst_set[u]:
                    distance = self.manhatt(points,v,u)
                    heapq.heappush(pq,(distance,u))
        return mst_weight

             



        