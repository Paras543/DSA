import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        max_heap = []
        for x,y in points:
            distance = x * x + y * y
            heapq.heappush(max_heap,(-distance,x,y))

            if len(max_heap)>k:
                heapq.heappop(max_heap) ## Inbuilt in python to remove the smallest element


        return [[x,y] for distance,x,y in max_heap]